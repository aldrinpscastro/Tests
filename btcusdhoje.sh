#!/usr/bin/env bash
valordolar=$(dolarhoje.sh | sed 's/.* // ; s/,/\./')
valorbtc=$(btchoje.sh | sed 's/.* // ; s/,/\./')
echo -n "US$ " ; echo "scale=2 ; $valorbtc / $valordolar" | bc | sed 's/\./,/'
