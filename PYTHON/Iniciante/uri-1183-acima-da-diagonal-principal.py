op = input()

matriz = []
soma, col, count = 0, 0, 0

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    
    matriz.append(linha)

for i in range(0,11,1):
    for j in range(11,col,-1):
        soma += matriz[i][j]
        count += 1
    
    col+=1
        

if op == "S":
    print("{:.1f}".format(soma))
elif op == "M":
    print("{:.1f}".format(soma / count))