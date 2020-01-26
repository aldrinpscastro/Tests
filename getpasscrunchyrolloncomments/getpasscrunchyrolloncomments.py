#!/usr/bin/env python3.6
import os
import sys
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from bs4 import BeautifulSoup
from time import sleep

delay = 3

try:
	urls = sys.argv[1:]
except IndexError:
	urls = 'https://www.crunchyroll.com/pt-br/dr-stone/episode-15-the-culmination-of-two-million-years-789328/comments'
	lang = 'English (US)'
	
if os.path.islink(sys.argv[0]) == True:
	dirname = os.path.dirname(os.readlink(sys.argv[0]))
else:
	dirname = '.'
	

options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options, executable_path=dirname + '/chromedriver')
langs = ("English (US)", "Español (América Latina)", "Português (Brasil)", "Français (France)")
try:
	while True:
		for url in urls:
			for language in langs:
				browser.get(url)
				element = browser.find_element_by_link_text(language)
				browser.execute_script("arguments[0].click()", element)
				pagina = browser.page_source
				pagina = pagina.split('</div>')[::-1]
				for line in pagina:
					if 'guestbook-body' in line:
						if '}}\n' not in line:
							line = re.sub('.*>', '', line)
							line = line.strip()
							print(line + '\n')
				print('----------------------FIM----------------------------')
				sleep(delay)
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
		os.system("wget -q https://www.reddit.com/r/anime/comments/cchojl/crunchyroll_guest_pass_thread/ -O - | sed 's/<\/p>/<\/p>\\n/g ; s/<p class=\"_1qeIAgB0cPwnLhDF9XSiJM\">/\\n<p class=\"_1qeIAgB0cPwnLhDF9XSiJM\">/g' | grep -i '<p class=\"_1qeIAgB0cPwnLhDF9XSiJM\">' | sed 's/<p class=\"_1qeIAgB0cPwnLhDF9XSiJM\">/<p class=\"_1qeIAgB0cPwnLhDF9XSiJM\">\\n/g' | grep -v '<p class=\"_1qeIAgB0cPwnLhDF9XSiJM\">' | sed 's/<\/.*>/\\n/g ; s/<del>//g' | sed 1,5d | tac")
		print('----------------------FIM----------------------------    ')
		sleep(delay)
except Exception as erro:
	print(erro)
	browser.quit()
	exit(0)
