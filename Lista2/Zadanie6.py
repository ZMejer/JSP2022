studenci = ['Kasia','Basia','Marek','Darek']
Ania_i_Basia = ['Ania', 'Basia']
studenci.append('Józek')
studenci.extend(Ania_i_Basia)
studenci = (sorted(studenci))
print(studenci)
print(studenci[3])
print(studenci[:2])
print(studenci[-2:])
while 'Basia' in studenci :
    studenci.remove('Basia')
print(len(studenci))
studenci_krotka = tuple(studenci)
print(studenci_krotka)