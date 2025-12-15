# Olvassuk be egy lista elemeinek számát, majd a lista elemeit. Számítsuk ki a lista
# pozitív elemeinek összegét.
n = int(input("Mennyi szamot akarsz meg adni?\n>"))
l = [0] * n
for i in range(n):
    print(i+1,"Szam")
    s = int(input(">"))
    l[i] = s
osszeg = 0    
for e in l:
    osszeg += e
print(l)
print(osszeg)