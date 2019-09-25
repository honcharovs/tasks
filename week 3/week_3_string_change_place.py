s = input()
posSpace = s.find(" ")
s1 = s[(posSpace + 1):] + " " + s[0:posSpace]
print(s1)
