import math
lista = []
for i in range(100,401):
    if i%2==0:
        dziesiatki = math.floor(i/10)
        if dziesiatki%2==0:
            setki = math.floor(dziesiatki/10)
            if setki%2==0:
                lista.append(i)
print(lista)
