"""
sublime_sequences.py
<1> - <Junjie Jiang>

Relevant comments:
-How long did this project take you to complete? 30 min
-Was there a particularly challenging part of the project? n/a
-Anything else you'd like to let us know? n/a

Some specifications and error handling:
- Most of the code in get_menu_choice() has been written for you, but
what happens when the user enters an invalid input (i.e. does not select
one of the menu options)? See if you can figure out a way to make your
code more ~ robust ~ by handling those cases.
- [IMPORTANT] If the user enters a negative number of terms, simply return
an empty list: []. Do not reprompt the user.
- If the user enters a negative number for positive_multiples(), return []
- Return all sequences as a list

"""


def get_menu_choice():
    x = input(
        "What sequence do you want to print? \n [1] Positive Odd Integers \n [2] Positive Integers in Multiples of x \n [3] Arithmetic Sequence \n [4] Geometric Sequence \n [5] Fibonacci Sequence \n Option: ")

    while x != "1" and x != "2" and x != "3" and x != "4" and x != "5":
        x = input(
            " Invalid Input   Try Again! \n What sequence do you want to print? \n [1] Positive Odd Integers \n [2] Positive Integers in Multiples of x \n [3] Arithmetic Sequence \n [4] Geometric Sequence \n [5] Fibonacci Sequence \n Option: ")

    n = int(input("\n What term do you want to go to? "))

    return x, n


def odd(n):
    list = []
    for a in range(1, 1 + 2 * n, 2):
        list.append(a)
    return list


def multiples(n):
    list = []
    for b in range(k, n * k, k):
        list.append(b)
    return list


def arithmatic(n):
    list = []
    for c in range(s, s + k * n, k):
        list.append(c)
    return list


def geometric(n):
    list = []
    q = s
    while n > 0:
        d = q * r
        list.append(d)
        q = d
        n = n - 1
    return list


def fibonacci(n):
    list = ['1']
    e = 0
    f = 1
    while n > 1:
        g = e + f
        list.append(g)
        e = f
        f = g
        n = n - 1
    return list


def print_sequence(seq):
    for i in seq:
        print(i)


def sublime_sequences():
    x, n = get_menu_choice()
    if x == "1":
        seq = odd(n)
    elif x == "2":
        k = input("Which multiple would you like to use?")
        seq = multiples(n, k)
    elif x == "3":
        s = input("What is the first term of the arithmetic sequence?")
        k = input("What is the second term of the arithmetic sequence?")
        seq = arithmatic(n, s, k)
    elif x == "4":
        s = input("What is the first term of the geometric sequence?")
        r = input("What is the second term of the geometric sequence?")
        seq = geometric(n, s, r)
    else:
        seq = fibonacci(n)

    print_sequence(seq)


if __name__ == "__main__":
    sublime_sequences()
