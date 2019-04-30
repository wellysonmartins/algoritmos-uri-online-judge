# -*- coding: utf-8 -*-

num = int(input())

a = int(num / 365)
m = int(num%365/30)
d = int(num%365%30)

print("{} ano(s)".format(a))
print("{} mes(es)".format(m))
print("{} dia(s)".format(d))