list1 = input().split()
minElement = 1000
for i in range(0, len(list1)):
    if 0 < int(list1[i]) <= minElement:
        minElement = int(list1[i])
print(minElement)
