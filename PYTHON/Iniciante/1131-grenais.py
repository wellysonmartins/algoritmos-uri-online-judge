x = 1
v_inter, v_gremio, empate = 0, 0, 0

while x == 1:
   inter, gremio = map(int, input().split(" "))

   if inter > gremio:
      v_inter+=1
   elif inter < gremio:
      v_gremio+=1
   else:
      empate+=1
   
   while True:
      print("Novo grenal (1-sim 2-nao)")
      x = int(input())
      if x == 1 or x == 2:
         break

grenais = v_inter + v_gremio + empate
print("{} grenais".format(grenais))
print("Inter:{}".format(v_inter))
print("Gremio:{}".format(v_gremio))
print("Empates:{}".format(empate))
if v_inter > v_gremio:
   print("Inter venceu mais")
elif v_gremio > v_inter:
   print("Gremio venceu mais")
else:
   print("Nao houve vencedor")