#!/usr/bin/env python3
import sys
import re
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from time import sleep

en = 'en'
es = 'es'
pt = 'pt'
if sys.argv[1] == en:
	lang = 'English (US)'
	
#en_gb = 'English (UK)'
if sys.argv[1] == es:
	lang = 'Español'
#es_es = 'Español (España)'
if sys.argv[1] == pt:
	lang = 'Português (Brasil)'
#pt_pt = 'Português (Portugal)'
#fr = 'Français (France)'
#de = 'Deutsch'
#ar = 'العربية'
#it = 'Italiano'
#po = 'Русский'

options = Options()
options.add_argument('--headless')
browser = webdriver.Firefox(options=options, executable_path='./geckodriver')
try:
	while True:
		browser.get('https://www.crunchyroll.com/dr-stone/episode-14-master-of-flame-789327/comments')
		browser.find_element_by_link_text(lang).click()
		pagina = browser.page_source
		pagina = pagina.split('</div>')[::-1]
		for line in pagina:
			if 'guestbook-body' in line:
				if '}}\n' not in line:
					line = re.sub('.*>', '', line)
					line = line.strip()
					print(line + '\n')
		print('--------------------------------------------------')
		sleep(2)
except KeyboardInterrupt:
	browser.quit()
	exit(0)

