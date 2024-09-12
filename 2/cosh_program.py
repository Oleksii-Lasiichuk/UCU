import math
x = float(input())

second_way = 0.5*(math.exp(x) + math.exp(-x))
third_way = 0.5*(math.e**x + math.e**(-x))

print(f"COS = {math.cosh(x):.4f}")
print(f"EXP = {second_way:.4f}")
print(f"E = {third_way:.4f}")