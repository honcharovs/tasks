n = int(input())
myList = list(map(int, input().split()))
x = int(input())
newList = []
if myList.count(x) > 0:
    print(x)
else:
    for i in range(n):
        newList.append(abs(myList[i] - x))
        closer = newList.index(min(newList))
print(myList[closer])
