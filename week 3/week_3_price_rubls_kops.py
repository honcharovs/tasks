from math import floor
price = float(input())
rubls = floor(price)
kops = (price - rubls) * 100
print(rubls, round(kops))
