list1 = input().split()
a = 0
for i in range(0, len(list1)):
    if int(list1[i]) > 0:
        a += 1
print(a)
