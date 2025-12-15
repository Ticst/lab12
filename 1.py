# Írjunk programot, mely a 10 és 30 közötti számok négyzeteit és köbeit állítja elő egy-
# egy listába.
n = []
k = []
for i in range(10,31):
    n.append(i**2)
    k.append(i**3)
print(n,'\n',k)