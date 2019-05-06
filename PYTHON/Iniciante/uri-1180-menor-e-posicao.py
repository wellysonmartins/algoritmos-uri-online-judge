n = int(input())
x = list(map(int, input().split()))

menor = min(x)
posicao = x.index(menor)

print("Menor valor: {}".format(menor))
print("Posicao: {}".format(posicao))