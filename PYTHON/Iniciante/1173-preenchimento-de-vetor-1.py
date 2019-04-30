num = int(input())

n = [num]
for i in range(9):
    n.append(n[i] * 2)

for i in range(10):
    print("N[{}] = {}".format(i,n[i]))