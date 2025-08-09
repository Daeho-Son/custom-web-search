import json
import re
import sys
import os

def is_include_keyword(shortcut_name, site_url_json):
    if site_url_json.get(shortcut_name) is None:
        return False
    return True


def display_shortcut_name(shortcut_name, site_url_json):
    if is_include_keyword(shortcut_name, site_url_json):
        yield {
            "uid": shortcut_name,
            "title": f"'{shortcut_name}' already exists.",
            "subtitle": "Enter the url you want to change in the next step.",
            "autocomplete": f"{shortcut_name} "
        }
    else:
        yield {
            "uid": shortcut_name,
            "title": f"Quick Shortcut to add : {shortcut_name}",
            "subtitle": "The added site can be executed through the 'go' keyword.",
            "autocomplete": f"{shortcut_name} "
        }


def build_alfred_process_items(shortcut_name, url=""):
    match = re.match(r'^(https?://)?[^/]+', url)
    base_url = match.group(0) if match else ''
    query_url = url

    yield {
        "uid": shortcut_name,
        "title": 'Enter url for search, but replace search term {search_query}',
        "subtitle": 'ex) https://www.google.com/search?q={search_query}',
        "arg": " ",
        "variables": {
            "shortcut_name": shortcut_name,
            "base_url": base_url,
            "query_url": query_url
        }
    }


def main():
    shortcut_name = sys.argv[1]
    site_url_json = json.loads(os.environ.get('URLS_JSON_CONTENT'))

    if len(sys.argv) > 2:
        url = sys.argv[2]
        items = list(build_alfred_process_items(shortcut_name, url))
    else:
        items = list(display_shortcut_name(shortcut_name, site_url_json))

    print(json.dumps({"items": items}))


main()
