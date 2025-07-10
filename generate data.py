import matplotlib.pyplot as plt #plt is alias for pyplot so you don't have to use pyplot over and over
#pyplot has several different functions to generate plots and charts
input_values = [1, 2, 3, 4, 5]
squares =[1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

#Set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#Set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

x_values = [4,6,3,5,1]
y_values = [2,3,6,9,15]
plt.scatter(x_values, y_values, s=100)

plt.show()

plt.savefig('squares_plot.png')