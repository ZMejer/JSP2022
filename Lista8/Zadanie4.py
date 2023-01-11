def poprawnosc(pesel):
    cyfry = list(pesel)
    a = int(cyfry[0])
    b = int(cyfry[1])
    c = int(cyfry[2])
    d = int(cyfry[3])
    e = int(cyfry[4])
    f = int(cyfry[5])
    g = int(cyfry[6])
    h = int(cyfry[7])
    i = int(cyfry[8])
    j = int(cyfry[9])
    k = int(cyfry[10])
    ostatniaCyfra = int(str(1*a + 3*b + 7*c + 9*d + 1*e + 3*f + 7*g + 9*h + 1*i + 3*j)[-1])
    if ostatniaCyfra == 0 and k == 0:
        return True
    elif 10-ostatniaCyfra == k:
        return True
    else:
        return False

def plec(pesel):
    cyfry = list(pesel)
    if int(cyfry[-2]) % 2 == 0:
        return "kobieta"
    else:
        return "mezczyzna"

def data(pesel):
    cyfry = list(pesel)
    miesiac = cyfry[2]+cyfry[3]
    dzien = cyfry[4]+cyfry[5]
    if int(miesiac[0]) == 8 or int(miesiac[0]) == 9:
        poczatekRoku = "18"
    elif int(miesiac[0]) == 0 or int(miesiac[0]) == 1:
        poczatekRoku = "19"
    elif int(miesiac[0]) == 2 or int(miesiac[0]) == 3:
        poczatekRoku = "20"
    elif int(miesiac[0]) == 4 or int(miesiac[0]) == 5:
        poczatekRoku = "21"
    elif int(miesiac[0]) == 6 or int(miesiac[0]) == 7:
        poczatekRoku = "22"

    if int(miesiac[0]) % 2 == 0:
        miesiac = "0"+miesiac[1]
    else:
        miesiac = str(int(miesiac) - int(miesiac[0])*10+10)

    rok = poczatekRoku+cyfry[0]+cyfry[1]

    data = dzien+"-"+miesiac+"-"+rok
    return data

try:
    with open("D:\Python\Lista8\PESEL.txt",'r') as plik:
        with open("D:\Python\Lista8\wyniki.txt",'w') as wyniki:
            numeryPesel = plik.read().split()
            for pesel in numeryPesel:
                if(poprawnosc(pesel)):
                    wyniki.write("nr PESEL: "+pesel+"\ndata urodzenia: "+data(pesel)+"\t plec: "+plec(pesel)+"\n\n") 
    plik.close()
    wyniki.close()
except:
    print("Plik nie istnieje.")