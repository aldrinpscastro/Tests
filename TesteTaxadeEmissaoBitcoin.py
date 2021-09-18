#!/usr/bin/env python3
from time import sleep

TaxaEmissao = 50
nbitcoins = 0
nblocos = 1
ano = 2009
nhavings = 0

while nbitcoins <= 21000000 or TaxaEmissao == 6.25:

    nbitcoins += TaxaEmissao

    nblocos += 1

    ano += 0.000019026

    if nblocos % 210000 == 0:

        nhavings += 1

        TaxaEmissao /= 2

#    sleep(0.001)

print(f'\nAno: {int(ano)}\nNº bloco: {nblocos}\nTx mineração: {TaxaEmissao}\nNº bitcoins: {nbitcoins}\nNº halving: {nhavings}')
