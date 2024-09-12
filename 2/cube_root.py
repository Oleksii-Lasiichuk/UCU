import math
a = int(input())
b = int(input())
c = int(input())
d = int(input())

first_formula = (-(b**3/27*a**3)) + (b*c/6*a**2) - (d/2*a)
second_formula = (c/3*a) - (b*b/9*a**2)

x = math.cbrt(first_formula + math.sqrt((first_formula**2)+(second_formula**3)) + first_formula - math.sqrt((first_formula**2)+(second_formula**3)))- b/3*a

print(f"{x:.2f}")