while True:
    num = [int(x) for x in input("").split()]

    if num[0] == 0: 
        break

    a, b = num[0] * num[1], 0

    while b * b * num[2]/100 <= a: 
        b += 1
        
    print(b - 1)