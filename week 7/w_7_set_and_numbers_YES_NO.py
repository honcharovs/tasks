myList = list(map(int, input().split()))
mySet = set()
for i in myList:
    if i in mySet:
        print('YES')
    else:
        print('NO')
    mySet.add(i)
