thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)   #output ['apple', 'blackcurrant', 'cherry']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]     #1:3 орнына осы сртрингтар
print(thislist)   #output ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)   #output ['apple', 'watermelon']

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)   #output ['apple', 'banana', 'watermelon', 'cherry']



