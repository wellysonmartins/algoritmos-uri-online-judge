t = int(input())
n = []
aux = 0
for i in range(1000):
   n.append(aux)
   aux += 1
   if aux == t:
      aux = 0
   
   print("N[{}] = {}".format(i,n[i]))