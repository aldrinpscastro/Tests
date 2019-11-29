#!/bin/bash
while true; do
wget -q https://www.crunchyroll.com/forumtopic-1046871/-tpico-oficial-passes-de-acesso-premium?pg=last -O - | sed -n '/<td class="showforumtopic-message-contents">/,/<\/td>/p' | sed 's/<td.*>\|<\/td>\|<div.*>\|<\/div>\|<span class=".*">\|<\/span>\|<br.*>\|<img.*>\|<a .*\|onclick.*\|<input.*\|value.*//g'
echo "-------------------------------------------------------------------"
sleep 2
done
