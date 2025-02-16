def countdown(n):
    return (i for i in range(n, -1, -1))
n = int(input("san engiz: "))
for number in countdown(n):
    print(number)