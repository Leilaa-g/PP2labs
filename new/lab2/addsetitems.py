thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)  #output {'orange', 'banana', 'cherry', 'apple'}

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)  #output {'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)   #output thisset {'banana', 'cherry', 'apple', 'orange', 'kiwi'}