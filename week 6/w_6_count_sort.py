def CountSort(marks):
    cntMarks = [0] * 101
    for mark in marks:
        cntMarks[mark] += 1
    for nowMark in range(101):
        print((str(nowMark) + ' ') * cntMarks[nowMark], end='')
marks = map(int, input().split())
CountSort(marks)
