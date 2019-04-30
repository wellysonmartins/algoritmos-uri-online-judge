# -*- coding: utf-8 -*-

num = float(input())

def flutuante(num, valor):
   num = float("{:.2f}".format(num))
   dinheiro = int(num/valor)
   return dinheiro

cem = flutuante(num, 100)
num -= cem*100

cinquenta = flutuante(num, 50)
num -= cinquenta*50

vinte = flutuante(num, 20)
num -= vinte*20

dez = flutuante(num, 10)
num -= dez*10.00

cinco = flutuante(num, 5)
num -= cinco*5

dois = flutuante(num, 2)
num -= dois*2

um = flutuante(num, 1)
num -= um*1

moeda_50 = flutuante(num, 0.50)
num -= moeda_50*0.50

moeda_20 = flutuante(num, 0.25)
num -= moeda_20*0.25

moeda_10 = flutuante(num, 0.10)
num -= moeda_10*0.10

moeda_5 = flutuante(num, 0.05)
num -= moeda_5*0.05

moeda_1 = flutuante(num, 0.01)
num -= moeda_1*0.01

print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(cem))
print("{} nota(s) de R$ 50.00".format(cinquenta))
print("{} nota(s) de R$ 20.00".format(vinte))
print("{} nota(s) de R$ 10.00".format(dez))
print("{} nota(s) de R$ 5.00".format(cinco))
print("{} nota(s) de R$ 2.00".format(dois))

print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(um))
print("{} moeda(s) de R$ 0.50".format(moeda_50))
print("{} moeda(s) de R$ 0.25".format(moeda_20))
print("{} moeda(s) de R$ 0.10".format(moeda_10))
print("{} moeda(s) de R$ 0.05".format(moeda_5))
print("{} moeda(s) de R$ 0.01".format(moeda_1))