import math

def zamiana(x,y,z,sposob):
    if (sposob=="rgb2hsv"):
        r = x/255
        g = y/255
        b = z/255
        Cmax = max(r,g,b)
        Cmin = min(r,g,b)
        roznica = Cmax-Cmin
        if(roznica==0):
            h = 0
        elif(Cmax == r):
            h = 60*(((g-b)/roznica)%6)
        elif(Cmax == g):
            h = 60*((b-r)/roznica +2)
        elif(Cmax == b):
            h = 60*((r-g)/roznica +4)
        if(Cmax == 0):
            s = 0
        else:
            s = (roznica/Cmax)*100
        v = Cmax*100
        print("RGB(",x,",",y,",",z,") = HSV(",h,"°,",s,"%,",v,"%)")
    if (sposob=="hsv2rgb"):
        h = x
        s = y/100
        v = z/100
        c = v*s
        a = c*(1-abs((h/60)%2-1))
        m = v-c
        if(0<=h<60):
            r1 = c
            g1 = a
            b1 = 0
        elif(60<=h<120):
            r1 = a
            g1 = c
            b1 = 0
        elif(120<=h<180):
            r1 = 0
            g1 = c
            b1 = a
        elif(180<=h<240):
            r1 = 0
            g1 = a
            b1 = c
        elif(240<=h<300):
            r1 = a
            g1 = 0
            b1 = c
        elif(300<=h<360):
            r1 = a
            g1 = c
            b1 = 0
        r = round((r1+m)*255)
        g = round((g1+m)*255)
        b = round((b1+m)*255)
        print("HSV(",h,"°,",s*100,"%,",v*100,"%) = RGB(",r,",",g,",",b,")")

sposob = input("Jak chcesz dokonac zamiany [rgb2hsv/hsv2rgb]")
x = int(input())
y = int(input())
z = int(input())
zamiana(x,y,z,sposob)