import requests
from bs4 import BeautifulSoup


def get_mana_url():
	url = 'https://nopiamanual.net/redirect-manatoki/'
	res = requests.get(url)
	soup = BeautifulSoup(res.text, 'html.parser')
	return soup.select("main#page-content p > a")[0]["href"]


if __name__ == '__main__':
	mana_url = get_mana_url()
	print(mana_url)
