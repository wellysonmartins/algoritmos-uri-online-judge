I, J = 0, 1
for i in range(11):
   for j in range(3):
      if (J == 1) or (J == 2) or (J == 3) or (J == 4) or (J == 5):
         print("I={} J={}".format(round(I), round(J)))
         J+=1
      else:
         print("I={:.1f} J={:.1f}".format(I, J))
         J+=1
   
   I += 0.2
   J = 1 + I