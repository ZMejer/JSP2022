import math
def zamiana(stopnie, sposob):
    if sposob == 'st2rad':
        print(stopnie," stopni w radianach to ",(stopnie*math.pi/180))
    elif sposob == 'rad2st':
        print(stopnie," radianow w stopniach to ",(stopnie*180/math.pi))

stopnie = int(input("Podaj wartosc "))
sposob = input("Podaj sposob zamiany [rad2st/st2rad]")
zamiana(stopnie,sposob)
