import math

#pi unicode: \u03C0
deg = input("Enter degrees: ")
rad = float(deg) * (math.pi/180)
simpRad = str(rad / math.pi) + '\u03C0'
print(rad)
print(simpRad)
