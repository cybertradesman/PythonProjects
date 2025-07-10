import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make many random walks, and plot the points
while True:
    rw = RandomWalk(40000)
    rw.fill_walk()

    plt.figure(dpi=128, figsize=(12,8))
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds, edgecolor='none', s=8)
    
    #Emphasize the first and last points.
    plt.scatter (0, 0, c='green', edgecolors='none', s=8)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolors='none', s=8)

    #Remove the axes for better visuals
    ax = plt.gca()
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)

    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break