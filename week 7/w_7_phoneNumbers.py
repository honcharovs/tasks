newNum = ''.join(i for i in input() if i.isdigit())
# print(newNum)
if len(newNum) == 7:
    newNum = '495' + newNum
elif len(newNum) == 11:
    newNum = newNum[-10:]
elif len(newNum) == 12:
    newNum = newNum[-10:]
# print(newNum)
phoneNums = []
for i in range(3):
    oldNum = ''.join(i for i in input() if i.isdigit())
    if len(oldNum) == 7:
        oldNum = '495' + oldNum
        phoneNums.append(oldNum)
    elif len(oldNum) == 11:
        oldNum = oldNum[-10:]
        phoneNums.append(oldNum)
    elif len(oldNum) == 12:
        oldNum = oldNum[-10:]
        phoneNums.append(oldNum)
# print(phoneNums)
for phoneNum in phoneNums:
    if newNum == phoneNum:
        print('YES')
    else:
        print('NO')
