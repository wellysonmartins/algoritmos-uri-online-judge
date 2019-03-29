h_inicial, h_final = map(int, input().split(" "))

if h_inicial >= h_final:
   duracao = (24-h_inicial) + h_final
else:
   duracao = h_final - h_inicial

print("O JOGO DUROU {} HORA(S)".format(duracao))