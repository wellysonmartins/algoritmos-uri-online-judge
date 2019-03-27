a, b, c = map(float, input().split(" "))

lista = [a, b, c]

i = 1
for i in range(len(lista)):
   for j in range(len(lista)-1):
      if lista[j] < lista[j+1]:
         lista[j], lista[j+1] = lista[j+1], lista[j]

a, b, c = lista[0], lista[1], lista[2]

if a >= b+c: print("NAO FORMA TRIANGULO")
elif pow(a,2) == pow(b,2)+pow(c,2): print("TRIANGULO RETANGULO")
elif pow(a,2) > pow(b,2)+pow(c,2): print("TRIANGULO OBTUSANGULO")
elif pow(a,2) < pow(b,2)+pow(c,2): print("TRIANGULO ACUTANGULO")

if a == b == c: print("TRIANGULO EQUILATERO")
elif (a==b) or (a==c) or (b==c): print("TRIANGULO ISOSCELES")
