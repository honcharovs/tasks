massive = list(map(int, input().split()))
lenMassive = len(massive)
for i in range(0, lenMassive - 1, 2):
    massive[i], massive[i + 1] = massive[i + 1], massive[i]
print(*massive)
