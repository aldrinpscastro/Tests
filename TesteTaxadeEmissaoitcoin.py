from time import sleep

TaxaEmissao = 50
nbitcoins = 0
nblocos = 1
ano = 2009
while TaxaEmissao > 0:
    if nblocos % 2048 == 0:
        TaxaEmissao /= 2
        ano += 0.038964992
    nbitcoins += TaxaEmissao
    nblocos += 1
    print(nblocos, int(ano))
    sleep(0.001)