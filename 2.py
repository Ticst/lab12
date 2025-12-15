# Töltsünk fel egy 10 elemű, egész elemekből álló listát 1 és 100 közötti véletlen
# számokkal. Számítsuk ki a lista elemeinek átlagát.
import random

l = [random.randint(1,100) for i in range(10)]
osszeg = 0
for i in range(len(l)):
    osszeg =+ l[i]
print(l)
print(osszeg/10)