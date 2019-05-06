a, b, c = map(float, input().split(" "))

delta = pow(b,2) - 4 * a * c
if (delta < 0) or (a == 0):
   print("Impossivel calcular")
else:
   r1 = (-b + pow(delta,1/2)) / (2 * a)
   r2 = (-b - pow(delta,1/2)) / (2 * a)
   print("R1 = {:.5f}".format(r1))
   print("R2 = {:.5f}".format(r2))