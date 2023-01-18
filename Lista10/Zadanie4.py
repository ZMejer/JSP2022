from xml.dom import minidom

class Kursy:
    def __init__(self,sciezka):
        self.sciezka = sciezka
    def listaKursow(self):
        plik = minidom.parse(self.sciezka)
        self.pozycje = plik.getElementsByTagName('nazwa_waluty')
        self.nazwy = []
        for elem in self.pozycje:
            self.nazwy.append(elem.firstChild.data)
        return self.nazwy
    def plnToCurr(self,curr,ilosc):
        plik = minidom.parse(self.sciezka)
        self.kod = plik.getElementsByTagName('kod_waluty')
        self.waluta = plik.getElementsByTagName('kurs_sredni')
        self.kursy = {}
        for i in range(len(self.kod)):
                self.kursy[self.kod[i].firstChild.data] = float(self.waluta[i].firstChild.data.replace(',','.'))
        return self.kursy[curr]*ilosc


kursy = Kursy("D:\Python\Lista10\kursy.xml")
wybor = int(input("1 - Lista dostepnych kursow \n2 - kowersja PLN <-> wybrana waluta \n3 - konwersja wybrana waluta <-> wybrana waluta\n"))
if(wybor==1):
    print("\n".join(kursy.listaKursow()))
elif(wybor==2):
    curr = input("Podaj kod waluty (np. USD)\n")
    ilosc = int(input("Podaj liczbe przeliczanych pieniedzy\n"))
    strona = int(input("W ktora strone chcesz zamienic \n1 - PLN -> wybrana waluta \n2 - wybrana waluta -> PLN\n"))
    if(strona==2):
        print(ilosc,curr,"to",kursy.plnToCurr(curr,ilosc),"PLN")
    elif(strona==1):
        print(ilosc,"PLN to",(ilosc*ilosc)/(kursy.plnToCurr(curr,ilosc)),curr)
elif(wybor==3):
    curr = input("Podaj kod waluty z ktorej chcesz zamienic\n")
    currDocelowa = input("Podaj kod waluty na ktora chcesz zamienic\n")
    ilosc = int(input("Podaj ilosc przeliczanych pieniedzy\n")) 
    wPLN = kursy.plnToCurr(curr,ilosc)
    wDocelowej = (wPLN*wPLN)/(kursy.plnToCurr(currDocelowa,wPLN))
    print(ilosc,curr,"to",wDocelowej,currDocelowa)


