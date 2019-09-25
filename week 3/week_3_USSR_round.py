from math import floor, ceil
x = float(input())
whole = floor(x)
fraction = x - whole
if fraction < 0.5:
    fraction = 0
else:
    fraction = 1
print(whole+fraction)
