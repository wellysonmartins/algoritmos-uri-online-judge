numeros = []
maior = 0
for i in range(100):
   numeros.append(int(input()))
   if numeros[i] > maior:
      maior = numeros[i]
      posicao = i + 1

print(maior)
print(posicao)