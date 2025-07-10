import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c='blue', edgecolor='red', s=20)

#Set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.scatter(500, 10000, c='green')

#Set the range for each axis.
plt.axis([0, 1100, 0, 1100000])

plt.show()