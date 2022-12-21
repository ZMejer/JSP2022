import random
import time
lista1 = []
for i in range(100):
    lista1.append(random.randint(0,20))

lista2 = []
for i in range(200):
    lista2.append(random.randint(0,20))

lista3 = []
for i in range(300):
    lista3.append(random.randint(0,20))

def sortowanie(lista):
    for i in range(1,len(lista)):
            tmp = lista[i]
            j = i-1
            while j>=0 and lista[j]>tmp:
                lista[j+1] = lista[j]
                j-=1
            lista[j+1] = tmp
    return lista


start_time1 = time.time()
print(sortowanie(lista1))
time1 = time.time() - start_time1

start_time2 = time.time()
print(sortowanie(lista2))
time2 = time.time() - start_time2

start_time3 = time.time()
print(sortowanie(lista3))
time3 = time.time() - start_time3

print("Czas dzialania dla stu elementow: ",time1)
print("Czas dzialania dla dwustu elementow: ",time2)
print("Czas dzialania dla trzystu elementow: ",time3)