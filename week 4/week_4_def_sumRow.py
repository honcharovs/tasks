def sumRow():
    a = int(input())
    if a != 0:
        a += sumRow()
    return a
print(sumRow())
