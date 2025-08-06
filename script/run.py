import json
import os
import sys


def parse_item_exclude_arg(item):
    return {
        "uid": item,
        "title": item,
        "subtitle": "Type a search keyword and press Enter or just Enter.",
        "autocomplete": f'{item} ',
        "icon": {
            "path": f"./logos/{item}.png"
        }
    }


def parse_item_include_arg(item, open_browser="", query=""):
    return {
        "uid": item,
        "title": item,
        "subtitle": f"Open/Search in {open_browser}",
        "arg": json.dumps({
            "site": item,
            "browser": open_browser,
            "query": query
        }),
        "autocomplete": f"{item + ' ' + query}",
        "icon": {
            "path": f"./logos/{open_browser}.png"
        }
    }


def find_matched_site_names(keyword, urls_data):
    for site_name in urls_data.keys():
        if keyword.lower() in site_name.lower():
            yield parse_item_exclude_arg(site_name)


def build_alfred_process_items(site_name, browsers, query):
    for browser in browsers:
        yield parse_item_include_arg(site_name, browser.strip(), query)

def is_include_keyword(keyword, site_url_json):
    if site_url_json.get(keyword) is None:
        return False
    return True

def main():
    keyword = sys.argv[1]
    browsers = os.environ.get('BROWSERS')
    site_url_json = json.loads(os.environ.get('URLS_JSON_CONTENT'))

    if len(sys.argv) > 2:
        query = ' '.join(sys.argv[2:])
        items = list(build_alfred_process_items(keyword, browsers.split(','), query))
    else:
        if not is_include_keyword(keyword, site_url_json):
            items = list(find_matched_site_names(keyword, site_url_json))
        else:
            items = list(build_alfred_process_items(keyword, browsers.split(','), ''))

    print(json.dumps({"items": items}))


main()
