import datetime as dt
import os

def deszyfrowanie(tekst, przesuniecie):
    deszyfrowane = ""
    for litera in tekst:
        if(97 <= ord(litera) <= 122):
            if(ord(litera)-przesuniecie<97):
                deszyfrowane+=chr(ord(litera)-przesuniecie+26)
            else:
                deszyfrowane+=chr(ord(litera)-przesuniecie)
        elif(65 <= ord(litera) <= 90):
            if(ord(litera)-przesuniecie<65):
                deszyfrowane+=chr(ord(litera)-przesuniecie+26)
            else:
                deszyfrowane+=chr(ord(litera)-przesuniecie)
        else:
            deszyfrowane+=litera
    return deszyfrowane

 
sciezka = input("Podaj sciezke do katalogu ")
dir_list = os.listdir(sciezka)
pliki = []
for file in dir_list:
    if "plik_zaszyfrowany" in file and file.endswith("txt"):
        pliki.append(file)

sciezkaDocelowa = input("Podaj sciezke do folderu, w ktorym ma byc zapisany nowy plik ")

try:
    if os.path.exists(sciezkaDocelowa):
        pass
    else:
        os.makedirs(sciezkaDocelowa)
except:
    print("Blad zapisu katalogow.")

try:
    for f in pliki:
        for i in range(1,11):
            if str(i)+"_" in f:
                przesuniecie = i
        with open(sciezka+"\\"+f,"r") as plik:
            try:
                tekst = plik.read()
            except:
                print("Blad odczytu pliku.")
            try:
                with open(sciezkaDocelowa+"\plik_deszyfrowany"+str(przesuniecie)+"_"+(dt.datetime.now().strftime("%Y"))+"-"+(dt.datetime.now().strftime("%m"))+"-"+(dt.datetime.now().strftime("%d"))+".txt","w") as docelowy:
                    docelowy.write(deszyfrowanie(tekst,przesuniecie))
                    docelowy.close()
            except:
                print("Blad zapisu pliku.")
            plik.close()
except:
    print("Nie mozna odnalezc pliku.")  


