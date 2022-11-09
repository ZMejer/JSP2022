m = int(input("Wprowadz wiersze"))
n = int(input("Wprowadz kolumny"))
for i in range(0,m):
    for j in range(0,n):
        print(i*j, end=" ")
    print("\n")
