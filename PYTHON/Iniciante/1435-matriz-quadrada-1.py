while True:
    n = int(input())
    matriz = []
    
    if n == 0:
        break
    
    for i in range(1,n+1,1):
        linha = []
        for j in range(1,n+1,1):
            x = i
            if j < x: x = j
            if (n-i+1) < x: x = n-i+1
            if (n-j+1) < x: x = n-j+1

            linha.append(x)
        
        matriz.append(linha)
        
    
    for i in range(n):
        aux = ''
        for j in range(n):
            aux += " {:3d}".format(matriz[i][j])
        
        print(aux[1:])
        
    print("")