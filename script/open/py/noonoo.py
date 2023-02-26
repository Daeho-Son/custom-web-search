import requests
from bs4 import BeautifulSoup


def get_noonoo_url():
	url = 'https://arca.live/b/noonoo/42211342?p=1'
	res = requests.get(url)
	soup = BeautifulSoup(res.text, 'html.parser')
	return soup.select('div.article-body p > a')[0]["href"]


if __name__ == '__main__':
	noonoo_url = get_noonoo_url()
	print(noonoo_url)
