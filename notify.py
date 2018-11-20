from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json
import time

def notification(title, message):
    import os
    cmd = 'ntfy -t "{0}" send "{1}"'.format(title, message)
    os.system(cmd)


def get_list():
	request = Request("https://www.olx.pl/nieruchomosci/mieszkania/wroclaw/")
	list = []
	request.add_header('User-Agent', 'Mozilla/5.0')
	with urlopen(request) as response:
		html_doc = response.read()
		soup = BeautifulSoup(html_doc, 'html.parser')
		offer_list = soup.find_all('div', class_='offer-wrapper')
		for offer in offer_list:
			title = offer.find('h3').get_text().strip()
			price = offer.find('p', class_='price').get_text().strip()
			url =  offer.find('h3').find('a').get('href').strip()
			list.append({'title': title, 'price': price, 'url': url})
	return list

def read_list_from_file():
	list = []
	try:
		with open('flats.json', 'r') as output:
			file_json = json.load(output)
	except Exception as error:
		print('exception: ',error)
		file_json = []
	for item in file_json:
		list.append(item)
	return list

def save_list_to_file(list):
	with open('flats.json', 'w') as input:
		json.dump(list, input)

def check_new():
	file_list = read_list_from_file()
	site_list  = get_list()
	is_new = False
	for site_item in site_list:
		already_in = False
		for file_item in file_list:
			if site_item['title'] == file_item['title']:
				already_in = True
				break
		if not already_in:
			#todo: add icon, and html body like a link direct to site
			message = site_item['title']
			notification('New Apartments for ' +site_item['price'], message)
			file_list.append(site_item)
			is_new = True
	save_list_to_file(file_list)

# main program

while 1:
	if not check_new():
		notification('Still checking...', "nothing new appeare, but it's time for a break")
	#
	# set time for sleep app
	#
	# 120: 2min (good for test)
	# 1200: 20min
	# 1800: 30min (25min work and 5 min break)

	time.sleep(1800)
