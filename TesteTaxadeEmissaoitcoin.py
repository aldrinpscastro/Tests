#!/usr/bin/env python3.6
from time import sleep

TaxaEmissao = 50
nbitcoins = 0
nblocos = 1
ano = 2009
while nbitcoins < 21000000:
    if nblocos % 210240 == 0:
        TaxaEmissao /= 2
    ano += 0.000019026
    nbitcoins += TaxaEmissao
    nblocos += 1
    print(nblocos, nbitcoins, TaxaEmissao, int(ano))
