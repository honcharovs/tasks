def ReduceFraction(a, b):
    a2 = a
    b2 = b
    while a2 != 0 and b2 != 0:
        if a2 > b2:
            a2 %= b2
        else:
            b2 %= a2
    nod = a2 + b2
    p = a/nod
    q = b/nod
    return int(p), int(q)
a = int(input())
b = int(input())
print(*ReduceFraction(a, b))
