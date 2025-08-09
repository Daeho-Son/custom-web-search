import json
import os
import sys


def find_matched_site_names(keyword, urls_data):
    for site_name in urls_data.keys():
        if keyword.lower() in site_name.lower():
            yield {
                "uid": site_name,
                "title": site_name,
                "subtitle": "Type a search keyword and press Enter or just Enter.",
                "autocomplete": f'{site_name} ',
                "icon": {
                    "path": f"./logos/{site_name}.png"
                }
            }


def build_alfred_process_items(item, browsers, query=""):
    for open_browser in browsers:
        open_browser = open_browser.strip()
        yield {
            "uid": item,
            "title": f"Search '{query}' in {item}" if query else f"Open {item}",
            "arg": " ",
            "variables": {
                "site": item,
                "browser": open_browser,
                "query": query
            },
            "autocomplete": f"{item + ' ' + query}",
            "icon": {
                "path": f"./logos/{open_browser}.png"
            }
        }


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
