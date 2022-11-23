def usuwanie(lista):
    for i in lista:
        x = lista.count(i)
        for j in range(0,x-1):
            lista.remove(i)

lista = [2,2,2,2,3,3,3,8,8]
print(lista)
usuwanie(lista)
print(lista)