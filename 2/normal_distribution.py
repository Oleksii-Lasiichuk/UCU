import math
pi = math.pi
e = math.e

x = float(input())
m = float(input())
sigma = float(input())

formula = (1/((2*pi*sigma**2)**0.5))* e**(-(x-m)**2/2*sigma**2)
print(f"{formula:.10f}")