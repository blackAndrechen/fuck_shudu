import requests
from bs4 import BeautifulSoup as BS

def crawl_shudu():
	url = input('please input shudu html:')
	
	response = requests.get(url).text
	soup = BS(response,'lxml')
	sdbody = soup.find('table',class_='ptb')

	shudu = []
	for tr in sdbody.find_all('tr'):
		trnum = []
		for td in tr.find_all('td'):
			num = td.find('input')['value']
			if num == '':
				trnum.append(0)
			else:
				trnum.append(int(num))
		shudu.append(trnum)
	
	return shudu
