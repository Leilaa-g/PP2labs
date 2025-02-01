#9
import math
def sphere(radius):
    V=(4*math.pi*(radius**3))/3
    return V
radius=float(input("Radius:"))
print(sphere(radius))