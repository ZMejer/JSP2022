import math

def obwod(a,b,c):
    return a+b+c

def pole(a,b,c):
    p = obwod(a,b,c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

def boki(a,b,c):
    if (a==b==c):
        return 'Trojkat jest równoboczny.'
    elif (a==b!=c or a==c!=b or b==c!=a):
        return 'Trojkat jest rownoramienny.'
    else:
        return 'Trójkąt jest różnoboczny.'

def katy(a,b,c):
    if(c*c>a*a+b*b or b*b>a*a+c*c or a*a>b*b+c*c):
        return 'Trojkat jest rozwartokątny.'
    elif(c*c==a*a+b*b or a*a==b*b+c*c or b*b==a*a+c*c):
        return 'Trojkat jest prostokątny.'
    else:
        return 'Trójką jest ostrokątny.'
