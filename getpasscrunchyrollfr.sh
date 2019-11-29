#!/bin/bash
while true; do
wget -q https://www.crunchyroll.com/forumtopic-924651/don-pass-invit-premium?pg=last -O - | sed -n '/<td class="showforumtopic-message-contents">/,/<\/td>/p' | sed 's/<td.*>\|<\/td>\|<div.*>\|<\/div>\|<span class=".*">\|<\/span>\|<br.*>\|<img.*>\|<a .*\|onclick.*\|<input.*\|value.*//g'
echo "------------------------------------------------------------------"
sleep 2
done
