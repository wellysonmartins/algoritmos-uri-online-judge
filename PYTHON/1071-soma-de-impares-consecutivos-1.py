x = int(input())
y = int(input())

if x < y:
   t = 1
else:
   t = -1

resultado = 0
for i in range(x+t, y, t):
   if i % 2 != 0:
      resultado += i

print(resultado)