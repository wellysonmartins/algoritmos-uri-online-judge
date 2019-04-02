count, soma = 0, 0
while True:
   idade = int(input())
   if idade < 0:
      break
   
   soma+=idade
   count+=1

print("{:.2f}".format(soma/count))