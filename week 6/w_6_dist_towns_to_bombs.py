n = int(input())  # количество поселений
list_n = list(map(int, input().split()))  # расстояние от дороги до поселений
m = int(input())  # количество б-у
list_m = list(map(int, input().split()))  # расстояние до б-у
# создаем список для сортировки поселений
sort_list_n = []
for i in range(0, n):
    sort_list_n.append([list_n[i], i, 0])
sort_list_n = sorted(sort_list_n)
# создаем список для сортировки бомбоубежищ
sort_list_m = []
for i in range(0, m):
    sort_list_m.append([list_m[i], i+1])
sort_list_m = sorted(sort_list_m)
# создаем список для расстояний от пос-й до б-у
dist_to_m = []
start = 0
for n_i in range(n):
    ind = 0
    minimum = 10e10
    for m_j in range(start, m):
        temp = abs(sort_list_n[n_i][0] - sort_list_m[m_j][0])
        if temp < minimum:
            ind = m_j
            minimum = temp
            sort_list_n[n_i][2] = sort_list_m[m_j][1]
        else:
            break
    start = ind
sort_list_n.sort(key=lambda x: x[1])
for i in range(0, n):
    print(sort_list_n[i][2], end=' ')
