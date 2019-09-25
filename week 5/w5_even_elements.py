list1 = input().split()
for i in range(0, len(list1)):
    if int(list1[i]) % 2 == 0:
        print(list1[i], end=' ')
