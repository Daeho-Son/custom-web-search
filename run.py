import json
import sys


def load_urls_from_json(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def parse_item(item, open_browser="", query=""):
    logo = item if open_browser == "" else open_browser.lower()
    subtitle = "Type a search keyword and press Enter or just Enter." if open_browser == "" else f"Open/Search in {open_browser}"
    return {
        "uid": item,
        "title": item,
        "subtitle": subtitle,
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

site_name = sys.argv[1]
urls_json_path = sys.argv[-1]
urls_data = load_urls_from_json(urls_json_path)
if len(sys.argv) > 3:
    search_terms = sys.argv[2:-1]
    query = ' '.join(search_terms)
else:
    query = ""

matching_sites = find_matching_sites(site_name, urls_data)

items = []
for site in matching_sites:
    items.extend([
        parse_item(site, "Google Chrome", query),
        parse_item(site, "Whale", query)
    ])


print(json.dumps({"items": items}))
