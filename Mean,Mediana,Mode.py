def solver(X, Y):
    sum = 0
    Y1=Y.split()
    for i in range(X):
        Y1[i]=int(Y1[i])
    for i in range(X):
        sum += Y1[i]
    u = sum / X
    print(u)

    Srednee = divmod(X, 2)
    Y1 = sorted(Y1)
    if Srednee[1] == 0:
        Median = (Y1[Srednee[0] - 1] + Y1[Srednee[0]]) / 2
    else:
        Median = Y1[Srednee[0]]
    print(Median)

    counter = 0
    Max1 = (Y1[0], 1)  # 1-element 2- znachenie counter
    for i in range(1, X):
        for j in range(i, X):
            if Y1[j] == Y1[i]:
                counter += 1
        if counter > Max1[1]:
            Max1 = (Y1[i], counter)
        counter = 0
    Mode = Max1[0]
    print(Mode)


num1 = int(input())
num2 = input()
solver(num1, num2)
# solver(10, (64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060))
