x = 1
while x == 1:
   count = 0
   media = 0
   while count < 2:
      nota = float(input())
      if 0 <= nota <= 10:
         media+=nota
         count+=1
      else:
         print("nota invalida")
   
   print("media = {:.2f}".format(media/2))
   while True:
      print("novo calculo (1-sim 2-nao)")
      x = int(input())
      if x == 1 or x == 2:
         break