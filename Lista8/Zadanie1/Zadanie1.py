import datetime as dt
import os

def szyfrowanie(tekst, przesuniecie):
    zaszyfrowane = ""
    for litera in tekst:
        if(97 <= ord(litera) <= 122):
            if(ord(litera)+przesuniecie>122):
                zaszyfrowane+=chr(ord(litera)+przesuniecie-26)
            else:
                zaszyfrowane+=chr(ord(litera)+przesuniecie)
        elif(65 <= ord(litera) <= 90):
            if(ord(litera)+przesuniecie>90):
                zaszyfrowane+=chr(ord(litera)+przesuniecie-26)
            else:
                zaszyfrowane+=chr(ord(litera)+przesuniecie)
        else:
            zaszyfrowane+=litera
    return zaszyfrowane

 
sciezka = input("Podaj sciezke do pliku ")
try:
    przesuniecie = int(input("Podaj przesuniecie "))
except:
    print("Przesuniecie musi byc liczba.")
sciezkaDocelowa = input("Podaj sciezke do folderu, w ktorym ma byc zapisany nowy plik ")

try:
    if os.path.exists(sciezkaDocelowa):
        pass
    else:
        os.makedirs(sciezkaDocelowa)
except:
    print("Blad zapisu katalogow.")

try:
    with open(sciezka,"r",encoding="utf-8") as plik:
        try:
            tekst = plik.read()
        except:
            print("Blad odczytu pliku.")
        try:
            with open(sciezkaDocelowa+"\plik_zaszyfrowany"+str(przesuniecie)+"_"+(dt.datetime.now().strftime("%Y"))+"-"+(dt.datetime.now().strftime("%m"))+"-"+(dt.datetime.now().strftime("%d"))+".txt","w") as docelowy:
                docelowy.write(szyfrowanie(tekst,przesuniecie))
                docelowy.close()
        except:
            print("Blad zapisu pliku.")
        plik.close()
except:
    print("Nie mozna odnalezc pliku.")  


