fruits = ("apple", "banana", "cherry")
print(fruits)  #output ('apple', 'banana', 'cherry')

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)   #output apple banana cherry

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)   #output apple ['mango', 'papaya', 'pineapple'] cherry
 