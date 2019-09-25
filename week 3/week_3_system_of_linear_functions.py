from math import floor, sqrt
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
deltaKramer = (a * d) - (c * b)
deltaX = (e * d) - (f * b)
x = deltaX / deltaKramer
deltaY = (a * f) - (c * e)
y = deltaY / deltaKramer
print(x, y)
