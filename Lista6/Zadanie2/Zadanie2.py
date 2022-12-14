import SzyfrCezara as szyfr

tekst = input()
print(szyfr.szyfrowanie(tekst))
print(szyfr.deszyfrowanie(szyfr.szyfrowanie(tekst)))