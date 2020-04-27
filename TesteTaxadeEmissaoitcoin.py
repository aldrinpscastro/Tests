#!/usr/bin/env python3.6
from time import sleep

TaxaEmissao = 50
nbitcoins = 0
nblocos = 1
ano = 2009
nhavings = 0

try:

    while nbitcoins <= 21000000:

        nbitcoins += TaxaEmissao
        nblocos += 1
        ano += 0.000019026
        if nblocos % 210000 == 0:
            nhavings += 1
            if TaxaEmissao > 0.00000001:
                TaxaEmissao /= 2
            else:
                TaxaEmissao = 0.00000001

finally:
    print(f'\nAno: {int(ano)}\nNº bloco: {nblocos}\nTx mineração: {TaxaEmissao}\nNº bitcoins: {nbitcoins}\nNº halving: {nhavings}')
    #sleep(0.0001)
