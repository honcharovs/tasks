from math import floor
percent = int(input())
depoRubls = int(input())
depoKops = int(input())
years = int(input())
depo = depoRubls * 100 + depoKops
i = 1
while i <= years:
    sumDepo = depo + depo * percent / 100
    depo = floor(sumDepo)
    i += 1
rubls = int(sumDepo // 100)
kops = floor((sumDepo % 100) * 100) / 100
print(rubls, int(kops))
