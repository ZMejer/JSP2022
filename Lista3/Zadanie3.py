import math
a = float(input("Podaj a"))
b = float(input("Podaj b"))
c = float(input("Podaj c"))
delta = pow(b,2)-(4*a*c)
if a==0:
    print("Nie jest to równanie kwadratowe")
elif delta>0:
    x1=((-b)-math.sqrt(delta))/(2*a)
    x2=((-b)+math.sqrt(delta))/(2*a)
    print("x1=",x1," x2=",x2)
elif delta<0:
    print("Równanie nie ma rozwiązań")
else:
    print("x=",-b/2*a)

