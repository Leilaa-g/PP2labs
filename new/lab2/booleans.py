print(10 > 9)    #output true
print(10 == 9)   #output false
print(10 < 9)    #output false

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
print(bool("Hello"))  #output true
print(bool(15))       #output true

x = "Hello"
y = 15
print(bool(x))     #output true
print(bool(y))     #true

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"]) #output true true true

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})   #output false false false false false

class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))  #output false

def myFunction() :
  return True
print(myFunction())   #output true

def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")   #output YES!
  
x = 200
print(isinstance(x, int))  #output true