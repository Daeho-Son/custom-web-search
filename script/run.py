import itertools
import json
import os
import sys


def parse_item(item, open_browser="", query=""):
    subtitle = "Type a search keyword and press Enter or just Enter." if open_browser == "" else f"Open/Search in {open_browser}"
    logo = item if open_browser == "" else open_browser
    return {
        "uid": item,
        "title": item,
        "subtitle": subtitle,
        "arg": json.dumps({
            "site": item,
            "browser": open_browser,
            "query": query
        }),
        "autocomplete": f"{item + ' '+ query}",
        "icon": {
            "path": f"./logos/{logo}.png"
        }
    }

def find_matched_site_name(keyword, urls_data):
    for site_name in urls_data.keys():
        if keyword.lower() in site_name.lower():
            yield parse_item(site_name)

def get_matched_site(keyword, urls_data):
    return urls_data.get(keyword)

def ff(site_name, browsers, query):
    for browser in browsers:
        yield parse_item(site_name, browser.strip(), query)


def main():
    keyword = sys.argv[1]
    browsers = os.environ.get('BROWSERS')
    site_url_json = json.loads(os.environ.get('URLS_JSON_CONTENT'))
    if len(sys.argv) > 2:
        query = ' '.join(sys.argv[2:])
        items=list(ff(keyword, browsers.split(','), query))
    else:
        items_generate = find_matched_site_name(keyword, site_url_json)
        items = list(itertools.islice(items_generate, 10))

    print(json.dumps({"items": items}))

main()