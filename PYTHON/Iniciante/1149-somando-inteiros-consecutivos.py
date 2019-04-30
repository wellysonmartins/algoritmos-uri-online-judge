numeros = map(int,input().split(" "))
num1, num2, soma = 0, 0, 0

for i in numeros:
    if(num1 == 0):
        num1 = i
    else:
        if(i > 0):
            num2 = i
            break

for i in range(num2):
    soma += num1
    num1 += 1
    
print("{}".format(soma))