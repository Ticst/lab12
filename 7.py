# Egy n fős csoport zárthelyi eredményeit kell kiértékelni. A pontszámhatárok a
# következők:
#  0 - 15 elégtelen
#  16 - 25 elégséges
#  26 - 35 közepes
#  36 - 45 jó
#  46 - 50 jeles
n = int(input("Mennyi szamot akarsz meg adni?\n>"))
l = [0] * n
uj = [0] * n
maxind = 0
minind = 0
for i in range(n):
    print(i+1,"Szam")
    s = int(input(">"))
    l[i] = s
ele = 0
tala = 0
koz = 0
jo = 0
jel = 0
for i in range(n):
    if l[i] < 0:

        print(l[i],"invalid")
    if l[i] > 0 and l[i] <= 15:
        ele += 1
    if l[i] > 15 and l[i] <= 25:
        tala += 1
    if l[i] > 25 and l[i] <= 35:
        koz += 1
    if l[i] > 35 and l[i] <= 45:
        jo += 1
    if l[i] > 45 and l[i] <= 50:
        jel += 1
print(ele,"elegtelen")
print(tala,"elegseges")
print(koz,"kozepes")
print(jo,"jo")
print(jel,"jeles")