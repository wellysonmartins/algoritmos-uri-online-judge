cod, qtd = map(int, input().split(" "))

tabela = {1:4.00,2:4.50,3:5.00,4:2.00,5:1.50}
total = qtd * tabela[cod]

print("Total: R$ {:.2f}".format(total))