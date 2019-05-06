n = int(input())

fibonacci = '0 1 '
a = 0
b = 1
for i in range(n-3):
   c = a+b
   fibonacci += str(c) + ' '
   a, b = b, c

c = a+b
fibonacci += str(c)
print(fibonacci)