import math


def axis():
    n = 10
    while n >= -10:
        if n != 0:
            k = str(n)
            l = len(k)
            s = 3 - l
            print(' ' * 30 + ' ' * s + k + '|' + ' ' * 30)
        else:
            rows()
            print('')
        n -= 1
    return


def rows():
    print('_' * 63)
    n = -10
    while n <= 10:
        k = str(n)
        l = len(k)
        s = 3 - l
        print(' ' * s + k, end='')
        n += 1
    return


def graph():
    totallength = 38
    height = 19
    start = 27 - 19
    base = 19
    current = 39
    for i in range(height):
        if current > 23:
            current -= 2
            start -= 1
            print(' ' * base + '|' + ' ' * start + '/' )
        elif current == 23:
            print('_' * totallength)
            current -= 1
        else:
            base -= 1
            print(' ' * base + '/' + ' ' * (18 - base) + '|')

    return





if __name__ == '__main__':
    print(graph())


