"""
tup = []

for i in range(3, 10):
    x, y = i, i ** 2
    tup.append((x, y))
print(tup)

"""

"""

sets = []
sets2 = []
for i in range(3, 10):
    sets.append(i)
for i in sets:
    sets2.append(i ** 2)

pew = []

for x in enumerate(sets2, 3):
    pew.append(x)

print(pew)

"""


""""
pewpew = {

}

sets = []
sets2 = []
for i in range(3, 10):
    sets.append(i)
for i in sets:
    sets2.append(i ** 2)

for i in range(len(sets)):
    pewpew[sets[i]] = sets2[i]
print(pewpew)

"""

"""
peww = {

}

for i in range(3, 10):
    peww[i] = i**2
print(peww)

"""

sets = []
for i in range(3,10):
    sets.append(i)
y = [x**2 for x in sets]

