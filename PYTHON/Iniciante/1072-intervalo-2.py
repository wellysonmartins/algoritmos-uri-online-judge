n = int(input())

n_in = 0
n_out = 0
for i in range(n):
   numero = int(input())
   if 10 <= numero <= 20:
      n_in += 1
   else:
      n_out += 1

print("{} in".format(n_in))
print("{} out".format(n_out))