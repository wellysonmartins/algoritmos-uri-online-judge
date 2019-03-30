n = int(input())

medias = []
for i in range(1,n+1,1):
   a, b, c = map(float, input().split(" "))
   medias.append(((a * 2) + (b * 3) + (c * 5)) / 10)

for i in range(n):
   print("{:.1f}".format(medias[i]))