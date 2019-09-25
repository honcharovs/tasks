def MinDivision(n):
    from math import sqrt
    i = 2
    while i <= n:
        if i <= sqrt(n):
            if n % i == 0:
                print(i)
                break
            else:
                i += 1
        else:
            print(n)
            break
n = int(input())
MinDivision(n)
