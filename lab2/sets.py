thisset = {"apple", "banana", "cherry"}
print(thisset)  #output {'cherry', 'banana', 'apple'}

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) #output {'banana', 'cherry', 'apple'}

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)  #output {False, True, 'cherry', 'apple', 'banana'}

thisset = {"apple", "banana", "cherry"}
print(len(thisset))  #output 3

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)   #output {'cherry', 'apple', 'banana'} {1, 3, 5, 7, 9} {False, True}

set1 = {"abc", 34, True, 40, "male"}
print(set1)  #output {True, 34, 40, 'male', 'abc'}

thisset = set(("apple", "banana", "cherry"))
print(thisset)   #output {'banana', 'cherry', 'apple'}
# Note: the set list is unordered, so the result will display the items in a random order.

myset = {"apple", "banana", "cherry"}
print(type(myset))  #output <class 'set'>