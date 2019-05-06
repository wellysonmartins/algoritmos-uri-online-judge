a, b, c = map(int, input().split(" "))

numeros = [a, b, c]
numeros_lidos = [a, b, c]

i = 1
for i in range(len(numeros)):
   for j in range(len(numeros)-1):
      if numeros[j] > numeros[j+1]:
         numeros[j], numeros[j+1] = numeros[j+1], numeros[j]

for i in range(len(numeros)):
   print(numeros[i])

print("")

for i in range(len(numeros_lidos)):
   print(numeros_lidos[i])