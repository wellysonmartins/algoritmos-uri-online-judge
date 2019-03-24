# -*- coding: utf-8 -*-

num = int(input())

valor = num

cem = num/100
aux = num%100

cinquenta = aux/50
aux = aux%50

vinte = aux/20
aux = aux%20

dez = aux/10
aux = aux%10

cinco = aux/5
aux = aux%5

dois = aux/2
aux = aux%2

um = aux/1

print(valor)
print("{} nota(s) de R$ 100,00".format(int(cem)))
print("{} nota(s) de R$ 50,00".format(int(cinquenta)))
print("{} nota(s) de R$ 20,00".format(int(vinte)))
print("{} nota(s) de R$ 10,00".format(int(dez)))
print("{} nota(s) de R$ 5,00".format(int(cinco)))
print("{} nota(s) de R$ 2,00".format(int(dois)))
print("{} nota(s) de R$ 1,00".format(int(um)))