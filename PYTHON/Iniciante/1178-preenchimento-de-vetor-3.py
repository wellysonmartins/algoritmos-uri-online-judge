x = float(input())
n = [x]
for i in range(1,100,1):
   n.append(n[i-1]/2)

for i in range(100):
   print("N[{}] = {:.4f}".format(i, n[i]))