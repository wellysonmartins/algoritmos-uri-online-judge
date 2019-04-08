n = int(input())

resposta = []

for i in range(n):
   numero = int(input())
   if numero == 0:
      resposta.append("NULL")
   else:
      if numero % 2 == 0:
         num = "EVEN"
      else:
         num = "ODD"
      
      if numero < 0:
         tipo = "NEGATIVE"
      else:
         tipo = "POSITIVE"
      
      resposta.append("{} {}".format(num, tipo))

for i in range(n):
   print(resposta[i])