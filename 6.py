# Olvassuk be egy lista elemeinek számát, majd a lista elemeit. Másoljuk át a lista
# elemeit egy másik listába úgy, hogy minden elem csak egyszer szerepeljen az új
# listában.
n = int(input("Mennyi szamot akarsz meg adni?\n>"))
l = [0] * n
uj = []
for i in range(n):
    print(i+1,"Szam")
    s = int(input(">"))
    l[i] = s
for e in l:
    if e not in uj:
        uj.append(e)
print("uj",uj,"\nregi",l)