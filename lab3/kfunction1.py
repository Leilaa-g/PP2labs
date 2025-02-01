#11
def palindrom(txt):
    if txt==txt[::-1]:
        print("Yes")
    else:
        print("No")
txt = input("Text: ")
palindrom(txt)