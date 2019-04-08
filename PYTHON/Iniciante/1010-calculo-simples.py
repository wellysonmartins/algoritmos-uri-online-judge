# -*- coding: utf-8 -*-

peca01, quant01, valor01 = input().split()
peca02, quant02, valor02 = input().split()

quant01 = float(quant01)
quant02 = float(quant02)
valor01 = float(valor01)
valor02 = float(valor02)

valor = (quant01 * valor01) + (quant02 * valor02)

print('VALOR A PAGAR: R$ {:.2f}'.format(valor))