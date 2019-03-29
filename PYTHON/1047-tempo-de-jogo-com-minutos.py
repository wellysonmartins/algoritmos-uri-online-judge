h_inicial, m_inicial, h_final, m_final = map(int, input().split(" "))

hora = h_final - h_inicial
if hora < 0:
   hora += 24

minuto = m_final - m_inicial
if minuto < 0:
   minuto += 60
   hora -= 1

if hora == 0 and minuto == 0:
   print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
   print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hora, minuto))