#2
def temperature(F):
    C = (5 / 9) * (F - 32)
    return C
F=float(input("Fahrenheit temperature:"))
print("Celsia:",temperature(F))