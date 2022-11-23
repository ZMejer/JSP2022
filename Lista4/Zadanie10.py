def nwd(a,b):
    if (a==b):
        print(a)
    elif(a>b):
        a=a-b
        nwd(a,b)
    elif(b>a):
        b=b-a
        nwd(a,b)

a = int(input("Podaj a "))
b = int(input("Podaj b "))
nwd(a,b)