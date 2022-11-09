liczba = int(input())
if(liczba%2==0):
    print(liczba, "jest parzysta")
else:
    print(liczba, "jest nieparzysta")

print(liczba, ["jest parzysta","jest nieparzysta"][liczba%2])