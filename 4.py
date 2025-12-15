# Olvassuk be egy lista elemeinek számát, majd a lista elemeit. Írassuk ki a legkisebb
# elemét és annak indexét is.
n = int(input("Mennyi szamot akarsz meg adni?\n>"))
l = [0] * n
for i in range(n):
    print(i+1,"Szam")
    s = int(input(">"))
    l[i] = s
minind = 0
maxind = 0
for i in range(n):
    if l[i] > l[maxind]:maxind = i
    if l[i] < l[minind]:minind = i
print("minindex es minszam",minind,l[minind])
print("maxindex es maxszam",maxind,l[maxind])