import numpy as np

# plot cos(x) in console using '+','|',' '
# each line of characters is one x location
NX = 40 # print out this many lines, covering a linear spacing from [0,2*pi]
NY = 80 # each line goes from [-1,1] in NY steps

x = np.linspace(0,2 * np.pi,NX).tolist()
print(x)