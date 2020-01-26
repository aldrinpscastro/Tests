#!/usr/bin/env python3.6
import subprocess
import re

source_code = subprocess.check_output(['wget', '-q', 'https://www.crunchyroll.com/videos/anime/alpha?group=all', '-O', '-'])

source_code = source_code.decode().split('\n')

lista_de_animes_da_crunchyroll_brasil = []

for line in source_code:
	if '<a title=' in line:
		begstring = line.index('"')
		endstring = line.index('"', begstring + 1)
		lista_de_animes_da_crunchyroll_brasil.append(line[begstring + 1:endstring])
with open('lista_animes_da_crunchyroll_Brasil.txt', 'w') as animes:
	for anime in lista_de_animes_da_crunchyroll_brasil:
		anime = re.sub(r'&amp;',r'&', anime)
		anime = re.sub(r'&quot;', r'"', anime)
		animes.write(anime + '\n')
	
