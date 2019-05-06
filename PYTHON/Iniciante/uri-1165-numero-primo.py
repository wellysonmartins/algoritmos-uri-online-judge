n = int(input())

for i in range(n):
   fatores = []
   num = int(input())
   for n in range(1,num+1):
      if num % n == 0:
         fatores.append(n)
         if len(fatores) > 2:
            print('{} nao eh primo'.format(num))
            break
   if len(fatores) == 2:
      print('{} eh primo'.format(num))