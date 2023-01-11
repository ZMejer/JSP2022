import numpy as np
import sys


if len(sys.argv) == 1:
    dane = []
    for i in sys.stdin:
        dane.append(int(i))
else:
    dane = sys.argv[1:]
    for i in range(len(dane)):
        dane[i] = int(dane[i])

srednia = np.average(dane)
wariancja = np.var(dane)
odchylenie = np.std(dane)
print("Wprowadzone dane: ",dane,' Srednia: ',srednia,' Wariancja: ',wariancja,' Odchylenie standardowe: ',odchylenie)

