def power2(a, n):
    def even(n):  # проверка четности
        if n % 2 == 0:
            return 1
        return 0
    if n == 0:
        return 1
    if n == 1:
        return a
    if even(n):
        return (power2(a, n/2) ** 2)
    return (a * power2(a, n-1))
a = float(input())
n = int(input())
print(power2(a, n))
