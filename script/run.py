import itertools
import json
import os
import sys


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

def find_matching_sites(search_term, urls_data, browsers, query):
    for site in urls_data.keys():
        if search_term.lower() in site.lower():
            for browser in browsers:
                yield parse_item(site, browser.strip(), query)


def main():
    site_name = sys.argv[1]
    browsers = os.environ.get('BROWSERS')
    urls_data = json.loads(os.environ.get('URLS_JSON_CONTENT'))
    if len(sys.argv) > 2:
        search_terms = sys.argv[2:]
        query = ' '.join(search_terms)
    else:
        query = ""

    items_generate = find_matching_sites(site_name, urls_data, browsers.split(','), query)
    items = list(itertools.islice(items_generate, 10))
    print(json.dumps({"items": items}))

main()