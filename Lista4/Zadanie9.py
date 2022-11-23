def silnia(n):
    wynik = 1
    for i in range(1,n+1):
        wynik*=i
    print(wynik)
    
n = int(input("Podaj n "))
silnia(n)