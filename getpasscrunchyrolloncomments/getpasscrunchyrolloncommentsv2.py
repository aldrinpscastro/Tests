#!/usr/bin/env python3.6
import os
import sys
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from bs4 import BeautifulSoup
from time import sleep

en = 'en'
es = 'es'
pt = 'pt'
delay = 3
try:
	urls = sys.argv[1:]
except IndexError:
	urls = 'https://www.crunchyroll.com/pt-br/dr-stone/episode-15-the-culmination-of-two-million-years-789328/comments'
	lang = 'English (US)'
	
#pt_pt = 'Português (Portugal)'
#fr = 'Français (France)'
#de = 'Deutsch'
#ar = 'العربية'
#it = 'Italiano'
#po = 'Русский'

if os.path.islink(sys.argv[0]) == True:
	dirname = os.path.dirname(os.readlink(sys.argv[0]))
else:
	dirname = '.'
	

options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(executable_path=dirname + '/chromedriver')
lang = ("English (US)", "Español (América Latina)", "Português (Brasil)", "Français (France)")
try:
	browser.get("https://www.crunchyroll.com/pt-br")
#	print(browser.find_elements_by_class_name("footer-language"))
	browser.find_element_by_xpath("//div[3]/div[2]/div[2]/div/div[1]/div[4]/ul/li[1]/a").click()
	
#	element = browser.find_element_by_link_text("English (US)")
#	browser.execute_script("arguments[0].click()", element)
#	pagina = browser.page_source
#	pagina = pagina.split('</div>')[::-1]
#	for line in pagina:
#		if 'guestbook-body' in line:
#			if '}}\n' not in line:
#				line = re.sub('.*>', '', line)
#				line = line.strip()
#				rint(line + '\n')
	print('----------------------FIM----------------------------')
	sleep(delay)
	os.system("wget -q https://www.crunchyroll.com/forumtopic-1046871/-tpico-oficial-passes-de-acesso-premium?pg=last -O - | sed -n '/<td class=\"showforumtopic-message-contents\">/,/<\/td>/p' | sed 's/<td.*>\|<\/td>\|<div.*>\|<\/div>\|<span class=\".*\">\|<\/span>\|<br.*>\|<img.*>\|<a .*\|onclick.*\|<input.*\|value.*//g'")
	print('----------------------FIM----------------------------')
	sleep(delay)
	os.system("wget -q https://www.crunchyroll.com/forumtopic-924651/don-pass-invit-premium?pg=last -O - | sed -n '/<td class=\"showforumtopic-message-contents\">/,/<\/td>/p' | sed 's/<td.*>\|<\/td>\|<div.*>\|<\/div>\|<span class=\".*\">\|<\/span>\|<br.*>\|<img.*>\|<a .*\|onclick.*\|<input.*\|value.*//g'")
	print('----------------------FIM----------------------------')
	sleep(delay)
	os.system("wget -q https://www.crunchyroll.com/forumtopic-803801/the-official-guest-pass-thread-read-opening-post-first?pg=last -O - | sed -n '/<td class=\"showforumtopic-message-contents\">/,/<\/td>/p' | sed 's/<td.*>\|<\/td>\|<div.*>\|<\/div>\|<span class=\".*\">\|<\/span>\|<br.*>\|<img.*>\|<a .*\|onclick.*\|<input.*\|value.*//g'")
	print('----------------------FIM----------------------------')
	sleep(delay)
except Exception as erro:
	print(erro)
	browser.quit()
	exit(0)
