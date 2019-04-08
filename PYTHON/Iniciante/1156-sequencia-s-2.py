s = 1
x = 2
for i in range(3,40,2):
   s += i/x
   x *= 2

print("{:.2f}".format(s))