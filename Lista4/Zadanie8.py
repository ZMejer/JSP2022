def harmoniczny(n):
    suma=1
    for i in range(2,n+1):
        suma+=(1/i)
    print(suma)

n = int(input("Podaj n "))
harmoniczny(n)