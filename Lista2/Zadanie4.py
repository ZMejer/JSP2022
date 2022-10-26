
napis = input()
pierwsza = napis[0]
zamienione = napis.replace(pierwsza, "$")
lista = list(zamienione)
lista[0] = pierwsza
print("".join(lista))