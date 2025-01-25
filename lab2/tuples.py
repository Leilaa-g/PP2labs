thistuple = ("apple", "banana", "cherry")
print(thistuple)   #output ('apple', 'banana', 'cherry')

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)   #output ('apple', 'banana', 'cherry', 'apple', 'cherry')

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))   #output  3

thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))   #output <class 'tuple'> <class 'str'>

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)   #output ('apple', 'banana', 'cherry') (1, 5, 7, 9, 3) (True, False, False)

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))   #output <class 'tuple'>

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)   #output ('apple', 'banana', 'cherry')