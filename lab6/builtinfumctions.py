#1
import math
numbers = list(map(int, input().split()))
result = math.prod(numbers)
print("The product of the list is:", result)

#2
st = str(input())
upper1 = 0
lower1 = 0
for i in st:
    if i.isupper():
        upper1+=1
    if i.islower():
        lower1+=1
print('lower:', lower1)
print('upper', upper1)

#3
string = str(input())
strint1 = string.lower().replace(' ', '')
reverse = strint1[::-1]
print(strint1 == reverse)

#4
import time
import math
san = int(input().strip())
second = float(input().strip())
time.sleep(second/1000)
print(f"Square root of {san} after {second} miliseconds is {math.sqrt(san)}")

#5
tuple = (True, 1, 1, 5)
print(all(tuple))