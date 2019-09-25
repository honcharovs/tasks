n = int(input())
list1 = list(map(int, input().split()))
x = int(input())
distanse = 2000
if massive.count(x) > 0:
    print(x)
else:
    for i in range(0, n):
        list2.append(abs(list1[i] - x))
    print(min(list2))
