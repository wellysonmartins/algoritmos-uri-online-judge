salario = float(input())

if 0 <= salario <= 400.00:
   percentual = 0.15
elif 400.01 <= salario <= 800.00:
   percentual = 0.12
elif 800.01 <= salario <= 1200.00:
   percentual = 0.10
elif 1200.01 <= salario <= 2000.00:
   percentual = 0.07
elif 2000.00 < salario:
   percentual = 0.04

reajuste = salario * percentual
novo_salario = salario + reajuste
percentual *= 100

print("Novo salario: {:.2f}".format(novo_salario))
print("Reajuste ganho: {:.2f}".format(reajuste))
print("Em percentual: {} %".format(int(percentual)))
