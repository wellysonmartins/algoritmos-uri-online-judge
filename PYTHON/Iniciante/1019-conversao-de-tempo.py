# -*- coding: utf-8 -*-
num = int(input())

count = h = m = s = 0

while num >= 60:
   m += 1
   num -= 60
   if m >= 60:
      h += 1
      m -= 60

s = num

print("{}:{}:{}".format(h, m, s))