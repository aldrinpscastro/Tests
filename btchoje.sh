#!/usr/bin/env bash
echo R$ $(wget -q https://www.mercadobitcoin.net/api/BTC/ticker/ -O - | sed 's/.*\"last\"://g ; s/,.*//g ; s/"//g  ; s/\./,/' | cut -b 1-8)
