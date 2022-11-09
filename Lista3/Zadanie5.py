import re
haslo=input()
wymagania = re.findall("[a-z]"and"[A-Z]"and"[0-9]"and"[$#@]",haslo)
if len(wymagania)>0 and 5<len(haslo)<17:
    print("Haslo spelnia wymagania")
else:
    print("Haslo nie spelnia wymagan")