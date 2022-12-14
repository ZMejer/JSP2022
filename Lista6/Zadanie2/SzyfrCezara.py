def szyfrowanie(tekst):
    szyfr = ""
    for i in tekst:
        if ord(i) in range (97,123):
            if ord(i) in range(110,123):
                szyfr += chr(ord(i)-13)
            else:    
                szyfr += chr(ord(i)+13)
        else:
            szyfr += chr(ord(i))
    return szyfr

def deszyfrowanie(tekst):
    szyfr = ""
    for i in tekst:
        if ord(i) in range (97,123):
            if ord(i) in range(110,123):
                szyfr += chr(ord(i)-13)
            else:    
                szyfr += chr(ord(i)+13)
        else:
            szyfr += chr(ord(i))
    return szyfr