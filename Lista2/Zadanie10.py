lista = list(range(0,100,3))
print(lista)
del(lista[4:len(lista):3])
print(lista)
print(sum(lista)/len(lista))