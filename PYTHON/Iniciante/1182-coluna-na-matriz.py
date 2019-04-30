num = int(input())
op = input()
matriz = []
soma = 0

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
                   
    matriz.append(linha)
    soma += matriz[i][num]

if op == "S":
    print("{:.1f}".format(soma))
elif op == "M":
    print("{:.1f}".format(soma / 12))