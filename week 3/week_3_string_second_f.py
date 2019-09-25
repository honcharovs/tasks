s = input()
i = 0
pos1 = s.find('f')
pos2 = s.rfind('f')
if pos1 == -1:
    print(-2)
elif pos1 == pos2:
    print(-1)
else:
    pos2 = s.find('f', (pos1 + 1))
    print(pos2)
