maxN = int(input())
# максимальное число, которое мог загадать Август
setN = set(range(1, maxN+1))  # создаем множество чисел, в которое входит число
augustSet = setN  # присваиваем множеству Августа возможное множество
line = input()  # Вводим первый ответ Беатрис
while line != 'HELP':
# Пока ответ Беатрис не равен ХЕЛП проверяем ответ с помощью IF на равенство YES, NO и другой вариант
    if line == 'YES':
        augustSet &= beatrisAns  # если ответ Беатрис равен YES, то augustSet &= beatrisAns
        # print(augustSet)
    elif line == 'NO':
        augustSet -= beatrisAns  # если ответ Беатрис равен NO, то augustSet -= beatrisAns
        # print(augustSet)
    else:
        beatrisAns = set(map(int, line.split()))  # если ответ Беатрис не YES и не NO, то это перечисление возможных вариантов от Беатрис через пробел
        # print(beatrisAns)
    line = input()  # После IF считываем ответ Беатрис (чтобы продолжился цикл while)
print(*sorted(augustSet))  # печатаем отсортированное множество оставшихся ответов в множестве Августа
