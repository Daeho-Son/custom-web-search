import json
import sys

def load_urls_from_json(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def parse_item(item, open_browser="", query=""):
    return {
        "uid": item,
        "title": item,
        "subtitle": "Type a search keyword and press Enter or just Enter." if open_browser == "" else f"Open/Search in {open_browser}",
        "arg": json.dumps({
            "browser": open_browser,
            "site": item,
            "query": query
        }),
        "autocomplete": f"{item} ",
        "icon": {
            "path": f"./logos/{item}.png"
        }
    }

def find_matching_sites(search_term, urls_data):
    return [site for site in urls_data.keys() if search_term.lower() in site.lower()]

def main():
    site_name = sys.argv[1]
    browsers = sys.argv[-2]
    urls_json_path = sys.argv[-1]
    urls_data = load_urls_from_json(urls_json_path)
    if len(sys.argv) > 4:
        search_terms = sys.argv[2:-2]
        query = ' '.join(search_terms)
    else:
        query = ""

    matching_sites = find_matching_sites(site_name, urls_data)

    items = []
    for site in matching_sites:
        for browser in browsers.split(','):
            items.extend([
                parse_item(site, browser.strip(), query),
            ])


    print(json.dumps({"items": items}))

main()