import copy

def permutacje(lista,n):
    for i in range(n, len(lista)):
        kolejna = copy.copy(lista)
        lista[i], lista[n] = lista[n], lista[i]
        permutacje(kolejna,n+1)
        if(n==len(lista)-1):
            lista[i], lista[0] = lista[0], lista[i]
    print(lista)
lista = [1, 2, 3] #123,132,213,231,312,321

lista1 = [1,2,3,4] #(1,2,3,4).(2,1,3,4).(3,1,2,4).(4,1,2,3).(1,2,4,3).(2,1,4,3).(3,1,4,2).(4,1,3,2).(1,3,2,4).(2,3,1,4).
                    #(3,2,1,4).(4,2,1,3).(1,3,4,2).(2,3,4,1).(3,2,4,1).(4,2,3,1).(1,4,2,3).(2,4,1,3).(3,4,1,2).(4,3,1,2).
                    # (1,4,3,2)(2,4,3,1)(3,4,2,1).(4,3,2,1).

permutacje(lista,0)
