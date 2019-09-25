list1 = input().split()
maxElement = 0
maxIndex = len(list1)
for i in range(len(list1)-1, -1, -1):
    if int(list1[i]) > maxElement:
        maxElement = int(list1[i])
        maxIndex = i
print(maxElement, maxIndex)
