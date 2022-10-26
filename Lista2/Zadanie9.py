import itertools
lista_poczatkowa = [[2,4,3],[1,5,6],[9],[7,9,0]]
zmiana = itertools.chain(*lista_poczatkowa)
lista = list(zmiana)
print(lista)