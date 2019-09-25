from math import floor
percent = int(input())
depoRubls = int(input())
depoKops = int(input())
depo = depoRubls * 100 + depoKops
depoWithPercent = floor(depo + depo / 100 * percent)
rubls = depoWithPercent // 100
kops = depoWithPercent % 100
print(rubls, kops)
