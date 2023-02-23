import pandas as pd


def stuff():
    xl = 'practical A.xlsx'
    df = pd.read_excel(xl)

    dt = df[['name', 'height', 'weight']]

    w = df['weight'].values.tolist()
    n = df['name'].values.tolist()

    total = 0
    for i in w:
        total += i

    average = total / len(w)

    pew = {

    }

    for i in range(len(n)):
        pew[w[i]] = n[i]

    w2 = []

    for i in range(len(w)):
        w2.append(abs(w[i] - average))

    x = 0
    y = True
    while y == True:
        for i in range(len(w2)):
            if x == w2[i]:
                return n[i], w[i], average
        x += 1


if __name__ == '__main__':
    print(stuff())
