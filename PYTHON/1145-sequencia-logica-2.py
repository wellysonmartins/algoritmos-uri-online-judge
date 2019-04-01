x, y = map(int, input().split(" "))

num = 0
while num < y:
   resultado = ''
   for i in range(x-1):
      num+= 1
      resultado += str(num) + ' '
   
   num+= 1
   resultado += str(num)
   
   print(resultado)