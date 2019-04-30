def square_digits(num):
   words = list(str(num))
   for word in words:
      print(int(word)**2, end="")

square_digits(input())