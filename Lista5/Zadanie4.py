def szyfrowanie(tekst):
    klucz = {'a' : 'y',
             'e' : 'i',
             'i' : 'o',
             'o' : 'a',
             'y' : 'e'}
    szyfr = ""
    for i in tekst:
        if i in klucz:
            szyfr += klucz[i]
        else:
            szyfr += i
    return szyfr

def deszyfrowanie(tekst):
    klucz = {'y' : 'a',
             'i' : 'e',
             'o' : 'i',
             'a' : 'o',
             'e' : 'y'}
    szyfr = ""
    for i in tekst:
        if i in klucz:
            szyfr += klucz[i]
        else:
            szyfr += i
    return szyfr

tekst = input()
print(szyfrowanie(tekst))
print(deszyfrowanie(szyfrowanie(tekst)))