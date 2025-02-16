def squares(a, b):
    return (num ** 2 for num in range(a, b + 1))
a = int(input("a: "))
b = int(input("b: "))
for square in squares(a, b):
    print(square)