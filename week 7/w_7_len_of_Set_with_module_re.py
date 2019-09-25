fin = open('input.txt', 'r', encoding='UTF-8')
fText = fin.read().rstrip().split()
fSet = set(fText)
print(len(fSet))
