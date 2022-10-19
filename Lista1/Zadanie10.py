import math
import cmath
z = complex(0,1)
print(z)
s = cmath.sin(z)
c = cmath.cos(z)
print("Część rzeczywista sin(z):",s.real)
print("Część urojona sin(z):",s.imag)
print("Część rzeczywista cos(z):",c.real)
print("Część urojona cos(z):",c.imag)
print(s**2 + c**2 == 1)
