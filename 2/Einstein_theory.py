from scipy.constants import c
m = float(input())
v = float(input())

mr = m / ((1-(v*v)/(c*c))**0.5)
e = mr*c*c
print(e)
