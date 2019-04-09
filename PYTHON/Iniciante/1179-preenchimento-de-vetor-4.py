v_par, v_impar = [], []
for i in range(15):
   num = int(input())
   if num % 2 == 0:
      v_par.append(num)
   else:
      v_impar.append(num)
   
   if len(v_par) == 5:
      for i in range(5):
         print("par[{}] = {}".format(i, v_par[i]))
      
      v_par.clear()
   
   if len(v_impar) == 5:
      for i in range(5):
         print("impar[{}] = {}".format(i, v_impar[i]))
      
      v_impar.clear()

for i in range(len(v_impar)):
   print("impar[{}] = {}".format(i, v_impar[i]))

for i in range(len(v_par)):
   print("par[{}] = {}".format(i, v_par[i]))