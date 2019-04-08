# -*- coding: utf-8 -*-
aux = 0
while aux == 0:
    X = int(input())
    for i in range(X-1):
        print('{} '.format(i+1), end='')

    if X == 0:
        aux = 1
    else:
        print(X)

