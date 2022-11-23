elementy = int(input("Podaj ile liczb chcesz dodac/przemnozyc ze soba "))
lista = []
for j in range(0,elementy):
    lista.append(int(input("Podaj element ")))
print(lista)


dzialanie=input("suma(+), iloczyn(*) czy suma i iloczyn(+*)? ")
if dzialanie=="+":
    x=0
    for i in range(0,len(lista)):
        lista[i] = int(lista[i])
        x+=lista[i]
    print("Wynik dodawania:",x)
elif dzialanie=="*":
    y=1
    for i in range(0,len(lista)):
        lista[i] = int(lista[i])
        y*=lista[i]
    print("Wynik mnozenia:",y)
elif dzialanie=="+*" or dzialanie=="*+":
    x=0
    for i in range(0,len(lista)):
        lista[i] = int(lista[i])
        x+=lista[i]
    print("Wynik dodawania:",x)
    y=1
    for i in range(0,len(lista)):
        lista[i] = int(lista[i])
        y*=lista[i]
    print("Wynik mnozenia:",y)   
else:
    print("Wprowadz prawidlowe dzialanie")