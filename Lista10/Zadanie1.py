import math

class Kolo():
    def __init__(self,r):
        self.r = r
    def pole(self):
        return str((self.r**2)*math.pi)
    def obwod(self):
        return str((2*math.pi*self.r))

test = Kolo(float(input("Wprowadz promien ")))
print("Pole: ",test.pole(),"\nObwod: ",test.obwod())