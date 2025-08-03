import sys
import json


def parse_item(item, open_browser, query=""):
    return {
        "uid":item,
        "title": f"{item} in {open_browser}",
        "subtitle": "Type a search keyword and press Enter or just Enter.",
        "arg": json.dumps({
            "browser": open_browser,
            "site": item,
            "query": query
        }),
        "autocomplete": f"{item} ",
        "icon": {
            "path": f"./logos/{open_browser.lower()}.png"
        }
    }

# TODO: [수정] 브라우저 하드코딩된 부분 리팩토링하기
items = []
site = ""
query = ""
if len(sys.argv) == 2:
    _, site = sys.argv
else:
    _, site, query = sys.argv
items = [
    parse_item(site, "Google Chrome", query),
    parse_item(site, "Whale", query)
]

print(json.dumps({"items": items}))