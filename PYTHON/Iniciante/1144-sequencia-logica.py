n = int(input())

for i in range(n):
   quadrado = pow(i+1,2)
   cubo = pow(i+1,3)
   print("{} {} {}".format(i+1, quadrado, cubo))
   print("{} {} {}".format(i+1, quadrado+1, cubo+1))