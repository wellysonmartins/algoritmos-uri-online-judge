dia_inicio = input()
hora_inicio = input()
hora_inicio = list(map(int, hora_inicio.split(" : ")))
dia_termino = input()
hora_termino = input()
hora_termino = list(map(int, hora_termino.split(" : ")))

di = int(dia_inicio.split()[1])
dt = int(dia_termino.split()[1])
hi = hora_inicio[0]
mi = hora_inicio[1]
si = hora_inicio[2]
ht = hora_termino[0]
mt = hora_termino[1]
st = hora_termino[2]

dia = dt - di

hora = ht - hi
if(hora < 0):
   hora = 24 + hora
   dia = dia - 1

minuto = mt - mi
if(minuto < 0):
   minuto = 60 + minuto
   hora = hora - 1

segundos = st - si
if(segundos < 0):
   segundos = 60 + segundos
   minuto = minuto - 1

if(dia <= 0):
   dia = 0

print ("{} dia(s)".format(dia))
print ("{} hora(s)".format(hora))
print ("{} minuto(s)".format(minuto))
print ("{} segundo(s)".format(segundos))




   
   