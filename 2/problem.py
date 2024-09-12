import math
r = float(input())
h = float(input())

pi = math.pi

v = h*r*r*pi
a = 2*h*pi*r + 2*pi*r*r

print(f'V = {v:.3f}')
print(f'A = {a:.3f}')