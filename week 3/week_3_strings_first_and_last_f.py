s = input()
if s.find('f') != -1:
    pos1 = s.find('f')
    pos2 = s.rfind('f')
    if pos1 == pos2:
        print(pos1)
    else:
        print(pos1, pos2)
else:
    print('')
