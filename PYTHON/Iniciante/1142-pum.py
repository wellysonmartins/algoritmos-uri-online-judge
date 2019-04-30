n = int(input())

num = 0
for i in range(n):
   resposta = ''
   for i in range(3):
      num += 1
      resposta += str(num) + ' '
   
   print("{}PUM".format(resposta))
   num+=1 