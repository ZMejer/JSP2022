import time

def fibonacciLoop(n):
    sequence = []
    if n == 1:
        sequence = [0]
    else:
        sequence = [0,1]
        for i in range(1, n-1):
            sequence.append(sequence[i-1] + sequence[i])
    print(sequence)

def fibonacciRecursion(n):
    if n in{0,1}:
        return n
    else:
        return fibonacciRecursion(n-1)+fibonacciRecursion(n-2)
    
n = input("Podaj n ")

start_time1 = time.time()
fibonacciLoop(int(n))
time1 = time.time() - start_time1
print("Czas dzialania petli: ",(time1))

start_time2 = time.time()
for i in range(int(n)):
    print(fibonacciRecursion(i), end=" ")
time2 = time.time() - start_time2
print("\nCzas dzialania rekurencji: ",(time2))