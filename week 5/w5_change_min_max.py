list1 = list(map(int, input().split()))
maxI = max(list1)
minI = min(list1)
list2 = list1.copy()
for i in range(0, len(list2)):
    if minI < list1[i] < maxI:
        i += 1
    elif list1[i] == maxI:
        list2[i] = minI
    elif list1[i] == minI:
        list2[i] = maxI
print(*list2)
