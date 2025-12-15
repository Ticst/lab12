# Olvassuk be egy lista elemeinek számát, majd a lista elemeit. Keressük meg az összes
# 2-nél nagyobb elemét és tegyük át ezeket egy új listába, majd írassuk ki.
n = int(input("Mennyi szamot akarsz meg adni?\n>"))
l = [0] * n
for i in range(n):
    print(i+1,"Szam")
    s = int(input(">"))
    l[i] = s
uj = []
for e in l:
    if e > 2:
        uj.append(e)
print(uj)