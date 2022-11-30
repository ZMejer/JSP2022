import math

def zamien(liczba):
    dict={1:'jeden',2:'dwa',3:'trzy',4:'cztery',5:'pięć',6:'sześć',7:'siedem',8:'osiem',9:'dziewięć',10:'dziesięć',
         11:'jedenaście',12:'dwanaście',13:'trzynaście',14:'czternaście',15:'piętnaście',16:'szesnaście',
         17:'siedemnaście',18:'osiemnaście',19:'dziewiętnaście',20:'dwadzieścia ',
         30:'trzydzieści ',40:'czterdzieści ',100:'sto ',200:'dwieście '}
    if(liczba>=1000):
        tysiace="tysiąc "
        liczba = liczba-1000
    else:
        tysiace=""

    if(liczba in range(100,300)):
        l1 = math.floor(liczba/100)*100
        setki = dict[l1]
        liczba = liczba-l1
    elif(liczba in range(300,500)):
        l1 = math.floor(liczba/100)*100
        setki = dict[l1//100]+'sta '
        liczba = liczba-l1
    elif(liczba in range(500,1000)):
        l1 = math.floor(liczba/100)*100
        setki = dict[l1//100]+'set '
        liczba = liczba-l1
    else:
        setki = ""

    if(liczba in range(20,50)):
        l2 = math.floor(liczba/10)*10
        dziesiatki = dict[l2]
        liczba = liczba - l2
    elif(liczba in range(50,100)):
        l2 = math.floor(liczba/10)*10
        dziesiatki = dict[l2//10]+'dziesiąt '
        liczba = liczba - l2
    elif(liczba in range(10,20)):
        dziesiatki = dict[liczba]
        liczba = 0
    else:
        dziesiatki=""

    if(liczba!=0):
        return tysiace+setki+dziesiatki+dict[liczba]

    else:
        return tysiace+setki+dziesiatki

liczba = int(input())
print(zamien(liczba))