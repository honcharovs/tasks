from math import floor, sqrt
a = float(input())
b = float(input())
c = float(input())
D = b ** 2 - 4 * a * c
if D > 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    if x2 < x1:
        (x1, x2) = (x2, x1)
    print(x1, x2)
elif D == 0:
    x = -b / (2 * a)
    print(x)
else:
    print("")
