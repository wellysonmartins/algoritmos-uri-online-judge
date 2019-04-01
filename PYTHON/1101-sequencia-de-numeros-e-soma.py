while True:
   m, n = map(int, input().split(" "))
   if m <= 0 or n <= 0:
      break

   soma = 0
   numeros = ''
   if m > n:
      for i in range(n, m+1, 1):
         soma+=i
         numeros += str(i) + ' '
   else:
      for i in range(m, n+1, 1):
         soma+=i
         numeros += str(i) + ' '
   
   numeros += 'Sum={}'
   print(numeros.format(soma))