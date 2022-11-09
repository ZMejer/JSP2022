N = int(input())
lista=[1,1]
if N==1: print("[1]")
else: 
    for i in range(3,N+1):
        kolejny = lista[i-3]+lista[i-2]
        lista.append(kolejny)
    print(lista)


