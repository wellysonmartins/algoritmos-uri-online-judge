# -*- coding: utf-8 -*-

num = int(input())

i = 0
while i < 6:
   if num % 2 == 0:
      num += 1
   
   print(num)
   i += 1
   num += 2
   
   