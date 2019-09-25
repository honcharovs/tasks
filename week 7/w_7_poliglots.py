class studLang():
    qnt = 0
    langs = []


def add_studLang(qnt, langs):
    stud = studLang()
    stud.qnt = qnt
    stud.langs = langs
    return stud

listStuds = []
setLangs = set()
studs = int(input())
i = 1
while i <= studs:
    qnt = int(input())
    j = 1
    langs = []
    while j <= qnt:
        l = input()
        langs.append(l)
        j += 1
    setLangs.update(langs)
    listStuds.append(add_studLang(qnt, langs))
    i += 1
everyKnowLang = setLangs.copy()
for elem in listStuds:
    everyKnowLang &= set(elem.langs)
print(len(everyKnowLang))
for lang in everyKnowLang:
    print(lang)
print(len(setLangs))
for elem in sorted(setLangs, reverse=True):
    print(elem)
