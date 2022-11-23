import math
def element(n, a1=1, q=2):
    an=a1*(pow(q,n-1))
    print(an)
n = int(input("Podaj n "))
a1 = float(input("Podaj a1 "))
q = float(input("Podaj q "))
element(n,a1,q)
element(n)