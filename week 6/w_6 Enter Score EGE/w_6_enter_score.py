inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
k = int(input())
rezult = []
l = inFile.readlines()
for i in l:
    if len(i.split()) == 6:
        n1, n2, n3, s1, s2, s3 = i.split()
    if len(i.split()) == 5:
        n1, n2, s1, s2, s3 = i.split()
    if int(s1) >= 40 and int(s2) >= 40 and int(s3) >= 40:
        sum = int(s1) + int(s2) + int(s3)
    else:
        sum = 0
    rezult.append(sum)
rezult.sort(reverse=True)
if rezult[k] == 0:
    print(0, file=fout)
elif rezult[0] == rezult[k]:
    print(1, file=fout)
elif rezult[k] == rezult[k - 1]:
    print(rezult[k - 2], file=fout)
else:
    print(rezult[k - 1], file=fout)
inFile.close()
outFile.close()
