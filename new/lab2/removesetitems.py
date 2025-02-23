thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)   #output {'cherry', 'apple'}

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)   #output {'apple', 'cherry'}

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)   #output set()

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) #this will raise an error because the set no longer exists

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item
print(thisset) #the set after removal    #output cherry {'apple', 'banana'}
