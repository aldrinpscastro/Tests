#!/usr/bin/env bash
echo R$ $(wget -q https://dolarhoje.com -O - | grep -i '<div id="cotacao">' | sed 's/.*id="nacional" value=//g ; s/\/><\/span><span class="optional">.*//g ; s/"//g')
