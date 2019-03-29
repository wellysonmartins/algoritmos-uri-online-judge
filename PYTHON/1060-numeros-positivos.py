qtd = 0
for i in range(6):
   numero = float(input())
   if numero > 0:
      qtd += 1

print("{} valores positivos".format(qtd))