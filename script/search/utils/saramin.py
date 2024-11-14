import requests
from bs4 import BeautifulSoup
import sys

def main():
    base_url = "https://www.saramin.co.kr"
    company_name = sys.argv[1]
    search_url = f'{base_url}/zf_user/search/company?searchword={company_name}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Whale/3.27.254.15 Safari/537.36"
    }
    url = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(url.text, 'html.parser')
    result = soup.select('div.item_corp > h2')[0]
    if result.find('a')['title'] in [f'(주){company_name}', company_name, f'{company_name}(주)']:
        print(base_url + result.find('a')['href'])
    else:
        print(search_url)

if __name__ == '__main__':
    main()
