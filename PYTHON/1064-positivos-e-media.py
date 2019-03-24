# -*- coding: utf-8 -*-

qtd_positivo = 0
total = 0
for i in range(6):
   num = float(input())
   if num > 0:
      qtd_positivo += 1
      total += num

media = total / qtd_positivo
print("{} valores positivos".format(qtd_positivo))
print("{:.1f}".format(media))