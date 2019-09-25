class Student:
    score = 0
    name = ''


def studentKey(student):
    return (-student.score, student.name)


n = int(input())
studentList = []
for i in range(n):
    tempManData = input().split()
    student = Student()
    student.score = int(tempManData[1])
    student.name = tempManData[0]
    studentList.append(student)
studentList.sort(key=studentKey)
for student in studentList:
    print(student.name)
