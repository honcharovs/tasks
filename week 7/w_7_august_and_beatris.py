fin = open('test1.txt', 'r', encoding='UTF-8')
maxN_fin = fin.read().split('\n')
maxN = int(maxN_fin[0])
# print(maxN)
setN = set(range(1, maxN+1))
# print(setN)
fText = maxN_fin
# print(fText)
i = 2
augustSet = setN
for line in fText:
    while line != 'HELP' and i < len(fText):
        if fText[i] == 'YES':
            beatrisAns = set(map(int, fText[i-1].split()))
            # print(beatrisAns)
            augustSet &= beatrisAns
            # print(augustSet)
        elif fText[i] == 'NO':
            beatrisAns = set(map(int, fText[i-1].split()))
            # print(beatrisAns)
            augustSet = augustSet - beatrisAns
            # print(augustSet)
        i += 2
print(*augustSet)
