import random
def generowanie():
    a = random.randint(0,9)
    b = random.randint(0,9)
    c = random.randint(0,9)
    d = random.randint(0,9)
    e = random.randint(0,9)
    f = random.randint(0,9)
    g = random.randint(0,9)
    h = random.randint(0,9)
    i = random.randint(0,9)
    j = random.randint(0,9)
    ostatniaCyfra = int(str(1*a + 3*b + 7*c + 9*d + 1*e + 3*f + 7*g + 9*h + 1*i + 3*j)[-1])
    if ostatniaCyfra == 0:
        k = 0
    else:
        k = 10 - ostatniaCyfra
    PESEL = str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(j)+str(k)
    return PESEL

with open('D:\Python\Lista8\PESEL.txt','w') as plik:
    for i in range(0,10):
        plik.write(generowanie()+'\n')
    plik.close()