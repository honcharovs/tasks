def summing(a, b):
    if b != 0:
        a += 1
        b -= 1
        if b > 0:
            return summing(a, b)
        else:
            return a
    elif b == 0:
        return a
a = int(input())
b = int(input())
print(summing(a, b))
