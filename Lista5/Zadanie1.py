def zamien(liczba):
    dict={'jeden':1, 'dwa':2, 'trzy':3, 'cztery':4, 'pięć':5, 'sześć':6, 'siedem':7, 'osiem':8, 'dziewięć':9, 'dziesięć':10,
          'jede':1, 'czter':4, 'pięt':5, 'szes':6, 'dziewięt':9, 'dwadzieścia':20}
    if 'naście' in liczba:
        liczbaLista = list(liczba)
        del liczbaLista[-6:]
        liczba = "".join(liczbaLista)
        return dict[liczba]+10
    elif 'dzie' in liczba:     
        liczba = liczba.split(" ")
        if 'ścia' in liczba[0]:
            if len(liczba) == 1:
                return dict[liczba[0]]
            elif len(liczba) == 2:
                return dict[liczba[0]]+dict[liczba[1]]
        elif 'ści' in liczba[0]:
            liczbaLista = list(liczba[0])
            del liczbaLista[-7:]
            liczba[0] = "".join(liczbaLista)
            if len(liczba)==2:
                return dict[liczba[0]]*10+dict[liczba[1]]
            elif len(liczba) ==1:
                return dict[liczba[0]]*10
        elif 'siąt' in liczba[0]:
            liczbaLista = list(liczba[0])
            del liczbaLista[-8:]
            liczba[0] = "".join(liczbaLista)
            if len(liczba)==2:
                return dict[liczba[0]]*10+dict[liczba[1]]
            elif len(liczba) ==1:
                return dict[liczba[0]]*10
    else:
        return dict[liczba]

liczba = input()
print(zamien(liczba))