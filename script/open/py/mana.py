import requests
from bs4 import BeautifulSoup


def get_mana_url():
	url = 'https://nopiamanual.net/%EB%A7%88%EB%82%98%ED%86%A0%EB%81%BC-manatoki/'
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
	}
	res = requests.get(url, headers=headers)
	soup = BeautifulSoup(res.text, 'html.parser')
	print(soup)
	return soup.select("main#page-content p > a")[0]["href"]


if __name__ == '__main__':
	mana_url = get_mana_url()
	print(mana_url)
