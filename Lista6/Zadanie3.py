def lookandsay(n):
        if (n == 1):
            print('1')
        if (n == 2):
            print('11')

        s = "11"
        print('1')
        print('11')
        for i in range(2, n):
            s += 'x' #po to bo inaczej jest string index out of range
            dlugosc = len(s)
            ilosc = 1 
            tmp = ""
            for j in range(1 , dlugosc):
                if (s[j] != s[j - 1]):
                    tmp += str(ilosc) 
                    tmp += s[j - 1]
                    ilosc = 1
                else:
                    ilosc += 1
            s = tmp
            print(s)

N = int(input("Podaj n "))
lookandsay(N)
