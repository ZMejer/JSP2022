def pascal(n):
    if n == 1:
        trojkat = [1]
        print(trojkat)
    elif n == 2:
        trojkat = [[1] ,[1, 1]]
        print(trojkat)
    else:
        trojkat=[[1], [1,1]]
        for i in range(2, n):
            kolejny = [1]
            for j in range(1, i):
                kolejny.append(trojkat[i-1][j-1] + trojkat[i-1][j])
            kolejny.append(1)
            trojkat.append(kolejny)
        for k in range(0,len(trojkat)):
            print(trojkat[k])

n = int(input("Podaj n"))
pascal(n)