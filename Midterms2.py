import numpy as np

# plot cos(x) in console using '+','|',' '
# each line of characters is one x location
NY = 40  # print out this many lines, covering a linear spacing from [0,2*pi]
NX = 80  # each line goes from [-1,1] in NY steps

x = np.linspace(0, 2 * np.pi, NY).tolist()
# math challenge :: we want to map [-1.0,1.0] (output of y = cos(x)) to [0,80] (integer locations along the output line we print).
# experimenting with such mappings would make a good practical test
xc = []
for i in x:
    xc.append(np.cos(i))

xi = []
xl = []

for i in xc:
    if i <= 0:
        xl.append((abs(i*40)))
    else:
        xl.append((i * 40 + 40))

for i in xc:
    if i <= 0:
        xi.append(round(abs(i*40)))
    else:
        xi.append(round(i * 40 + 40))


for i in range(len(x)):
    print('{} | {:05f} | {:05f} | {:.05f} | {}'.format(i, x[i], xc[i], xl[i], xi[i]))


# iterate over NX lines of x
#   iterate over NY characters per line
#       print the correct '+','|',' '
#   terminate the line


for i in range(len(xi)):
    if xi[i] <= 40:
        print(str(i) + ' ' * (41 - xi[i] - 1) + '+' + ' ' * (xi[i] - 1) + '|' + ' ' * 40)

    else:
        print(str(i) + ' ' * 40 + '|' + ' ' * (xi[i] - 41) + '+' + ' ' * (80 - xi[i]))

pass

