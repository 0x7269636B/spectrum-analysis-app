import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, color='blue')  # Try changing the color if it's not visible
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')

plt.show()
