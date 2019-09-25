fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
studs = []
for stud in fin.readlines():
    if list(stud.split()):
        studs.append([list(stud.split())[0] + ' ' + list(stud.split())[1],
                      list(stud.split())[2], list(stud.split())[3], ])
# print(students)
studs.sort(key=lambda s: s[0].casefold())
studs_out = []
for student in studs:
    student = [student[0], student[-1]]
    print(*student)
# fout.close()
