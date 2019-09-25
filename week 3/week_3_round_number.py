import math
n = float(input())
b = 0
if n > 1:
    b = math.floor(n)
    c = n % b
else:
    c = n
print(c)
