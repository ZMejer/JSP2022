import trojkat

a = int(input("Podaj dlugosc 1. boku"))
b = int(input("Podaj dlugosc 2. boku"))
c = int(input("Podaj dlugosc 3. boku"))

if(a+b<c or a+c<b or b+c<a):
    print('Z podanych dlugosci nie mozna zbudowac trojkata')
else:
    print('Obwod wynosi ',trojkat.obwod(a,b,c),'. Pole wynosi ',trojkat.pole(a,b,c),'. ',trojkat.boki(a,b,c),trojkat.katy(a,b,c))