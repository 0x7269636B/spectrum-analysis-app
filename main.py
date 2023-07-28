'''
import PySimpleGUI as sg

sg.Window(title="", layout=[[]], margins=(100, 50)).read()
'''

import matplotlib.pyplot as plt

# Import data from file
#open file
file = open("random.txt", "r")

counter = 0
x = []
y = []
while file.readline() != "":
    line = file.readline()
    index = 0
    x_axis = [line.split(",")[index]]
    x_axis = [int(item.replace("\n", "")) for item in x_axis]
    index = 1
    y_axis = [line.split(",")[index]]
    y_axis = [int(item.replace("\n", "")) for item in y_axis]
    x.append(x_axis)
    y.append(y_axis)
    counter += 1
    

# Create the plot
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 1)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Zoom In Chart Example')

# Set the initial limits of the plot
plt.xlim(0, counter+1000)
plt.ylim(0, 2000)

# Show the initial plot
plt.show()

# Now, let's zoom in on a specific region
zoomed_x_range = [2.5, 4]
zoomed_y_range = [4, 9]

# Set the new limits for the zoomed region
plt.xlim(zoomed_x_range)
plt.ylim(zoomed_y_range)

# Show the zoomed plot
plt.show()
