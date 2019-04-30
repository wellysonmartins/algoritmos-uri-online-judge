x = int(input())
while True:
   z = int(input())
   if z > x:
      break

soma = 0
qtd = 0
for i in range(x, z+1, 1):
   if soma < z:
      qtd+=1
   
   soma+=i

print(qtd)