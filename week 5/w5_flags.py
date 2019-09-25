n = int(input())

print('+___ ' * n)
for i in range(1, n+1):
    s = '|' + str(i) + ' / '
    print(s, end='')
print('')
print('|__\ ' * n)
print('|    ' * n)
