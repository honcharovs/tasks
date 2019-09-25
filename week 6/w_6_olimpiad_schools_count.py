class SchoolOlimp:
    surname = ''
    name = ''
    school = 0
    score = 0


class School:
    number = 0


fin = open('input.txt', 'r', encoding='utf-8')
listSchool = []
for i in fin.readlines():
    if list(i.split()):
        school = School()
        school.number = int(i.split()[-2])
        listSchool.append(school.number)


def CountSort(schools):
    cntSchools = [0] * 101
    for school in schools:
        cntSchools[school] += 1
    return cntSchools

# print(listSchool)
CountSort(listSchool)
# print(CountSort(listSchool))
# print(max(CountSort(listSchool)))
for i in range(101):
    if CountSort(listSchool)[i] == max(CountSort(listSchool)):
        print(i, end=' ')
