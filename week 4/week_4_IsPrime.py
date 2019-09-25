def IsPrime(n):
    from math import sqrt
    i = 2
    while i <= n:
        if i <= sqrt(n):
            if n % i == 0:
                return i == n or i == 1
                break
            else:
                i += 1
        else:
            return True
            break
n = int(input())
if IsPrime(n):
    print("YES")
else:
    print('NO')
