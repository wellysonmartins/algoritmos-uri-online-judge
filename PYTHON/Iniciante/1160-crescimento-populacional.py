t = int(input())

for i in range(t):
   pa, pb, g1, g2 = input().split()
   pa, pb = int(pa), int(pb)
   g1, g2 = float(g1), float(g2)
   
   anos = 0
   while pa <= pb:
      pa += int(pa*(g1/100))
      pb += int(pb*(g2/100))
      anos += 1

      if anos > 100:
         break
   
   if anos > 100:
      print("Mais de 1 seculo.")
   else:
      print("{} anos.".format(int(anos)))