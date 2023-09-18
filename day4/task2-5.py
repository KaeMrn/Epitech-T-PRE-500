n = int(input("Please enter an integer: "))

for i in range(2, n//2+1):
    multiples=[]

    for j in range(i, n, i):
        multiples.append(j)

    print(*reversed(multiples))