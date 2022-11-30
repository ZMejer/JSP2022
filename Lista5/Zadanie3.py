def zamiana(liczba):
    dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    dziesietnie = 0
    if(liczba in ['I','V','X','L','C','D','M']):
        return dict[liczba]
    else:
        for i in range(0,len(liczba)-1):
            przed = liczba[i]
            po = liczba[i + 1]
            if dict[przed] < dict[po]:
                dziesietnie -= dict[przed]
            else:
                dziesietnie += dict[przed]
        dziesietnie += dict[liczba[-1]]
        return dziesietnie

liczba = input()
print(zamiana(liczba))