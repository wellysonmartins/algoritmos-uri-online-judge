n = []
for i in range(20):
    n.append(int(input()))

j = 19
for i in range(10):
    aux = n[i]
    n[i] = n[j]
    n[j] = aux
    j-=1

for i in range(20):
    print("N[{}] = {}".format(i, n[i]))