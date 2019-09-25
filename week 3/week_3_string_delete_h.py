s = input()
posStart = s.find('h')
posEnd = s.rfind('h')
s2 = s[0:posStart] + s[(posEnd + 1):]
print(s2)
