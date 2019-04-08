f = [0,1]
a, b = 0, 1
for i in range(60):
   n = a + b
   f.append(n)
   a = b
   b = n

t = int(input())
for i in range(t):
   n = int(input())
   print("Fib({}) = {}".format(n, f[n]))