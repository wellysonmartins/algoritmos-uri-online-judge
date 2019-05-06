while True:
    n = int(input())
    matriz = []

    if n == 0:
        break

    for i in range(1,n+1,1):
        linha = []
        
        for j in range(i,1,-1):
            linha.append(j)

        qtd = len(linha)
        for k in range(1,n+1-qtd,1):
            linha.append(k)
        
        matriz.append(linha)
        
    
    for i in range(n):
        aux = ''
        for j in range(n):
            aux += " {:3d}".format(matriz[i][j])
        
        print(aux[1:])
        
    print("")