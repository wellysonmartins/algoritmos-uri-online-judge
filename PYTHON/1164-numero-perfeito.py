n = int(input())

for i in range(n):
   x = int(input())
   soma = 0
   for i in range(1,x,1):
      if x % i == 0:
         soma+=i
   
   if soma == x:
      print("{} eh perfeito".format(x))
   else:
      print("{} nao eh perfeito".format(x))