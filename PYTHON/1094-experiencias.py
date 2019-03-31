n = int(input())

cobaias = {"C":0,"R":0,"S":0}

total = 0
for i in range(1,n+1,1):
   qtd, cobaia = map(str, input().split(" "))
   cobaias[cobaia] += int(qtd)
   total += int(qtd)

print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(cobaias["C"]))
print("Total de ratos: {}".format(cobaias["R"]))
print("Total de sapos: {}".format(cobaias["S"]))
print("Percentual de coelhos: {:.2f} %".format((cobaias["C"] / total) * 100))
print("Percentual de ratos: {:.2f} %".format((cobaias["R"] / total) * 100))
print("Percentual de sapos: {:.2f} %".format((cobaias["S"] / total) * 100))