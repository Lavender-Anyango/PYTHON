def myAstericks(n):
    for i in range(1, n+1):
        for j in range(1 , i + 1):
            print('*', end='')
        print()

myAstericks(5)


def myAstericks2(n):
    for i in range(n +1, 1):
        for j in range(i + 1 , 1):
            print('*', end='')
        print()

myAstericks2(5)