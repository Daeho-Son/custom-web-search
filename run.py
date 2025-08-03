import json
import sys


def load_urls_from_json(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def parse_item(item):
    return {
        "uid": item,
        "title": item,
        "subtitle": "Press Enter to proceed to the next step.",
        "arg": f"{item} ",
        "autocomplete": f"{item} ",
        "icon": {
            "path": f"./logos/{item}.png"
        }
    }


_, query, urls_json_path = sys.argv
urls_data = load_urls_from_json(urls_json_path)  # JSON 파일 읽기
items = [parse_item(site) for site in urls_data if query in site]

print(json.dumps({"items": items}))
