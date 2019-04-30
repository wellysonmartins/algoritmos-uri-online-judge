n = int(input())

soma = 0
resultado = []
for i in range(n):
   x, y = map(int, input().split(" "))
   if x == y:
      soma = 0
   elif x < y:
      for j in range(x+1,y,1):
         if j % 2 != 0:
            soma += j
   elif y < x:
      for k in range(x-1,y,-1):
         if k % 2 != 0:
            soma += k
   
   resultado.append(soma)
   soma = 0

for i in range(n):
   print(resultado[i])