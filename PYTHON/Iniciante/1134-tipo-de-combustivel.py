alcool, gasolina, diesel = 0, 0, 0

while True:
   while True:
      cod = int(input())
      if 0 < cod < 5:
         break
   
   if cod == 1: alcool+=1
   elif cod == 2: gasolina+=1
   elif cod == 3: diesel+=1
   else: break

print("MUITO OBRIGADO")
print("Alcool: {}".format(alcool))
print("Gasolina: {}".format(gasolina))
print("Diesel: {}".format(diesel))