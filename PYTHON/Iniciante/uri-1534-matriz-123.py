while True:
    try:
        n = int(input())

        matriz = []

        count = n-1
        for i in range(n):
            linha = []
            for j in range(n):
                if j == count:
                    linha.append(2)
                    count -= 1
                else:
                    if i == j:
                        linha.append(1)
                    else:
                        linha.append(3)
                
            matriz.append(linha)
        
        for i in range(n):
            aux = ''
            for j in range(n):
                aux += str(matriz[i][j])
            
            print(aux)
    except EOFError:
        break

