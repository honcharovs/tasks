list1 = input().split()
for i in range(0, len(list1)):
    if i+1 < len(list1):
        if int(list1[i+1]) > int(list1[i]):
            print(list1[i+1], end=' ')
        i += 1
