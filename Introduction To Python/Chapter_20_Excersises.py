# Things to do, chapter 20
import matplotlib.pyplot as plt

# The exercises are going to make us three plots, so I'm setting up three subplots beforehand.
# This way we can display all the plots from the exercises at the same time.
_, plts = plt.subplots(nrows=1, ncols=3)

# 20.1 Install matplotlib. Draw a scatter diagram of these (x, y) pairs: ( (0, 0), (3, 5), (6, 2), (9, 8), (14, 10) ).
print("\n------ 20.1 ------")

# Create our data
pairs = ((0, 0), (3, 5), (6, 2), (9, 8), (14, 10))
x, y = zip(*pairs)

# Scatter them on the plot and display them
# The plot.show() is used at the bottom of this script, so we can add the other exercises along the way
plts[0].scatter(x, y)
print("Scatter plot done")


# 20.2 Draw a line graph of the same data.
print("\n------ 20.2 ------")
plts[1].plot(x, y)
print("Graph plot done")

# 20.3 Draw a plot (a line graph with markers) of the same data.
print("\n------ 20.3 ------")
plts[2].plot(x, y, 'o-')
print("Marker Graph plot done\n")

print("Displaying plots")
# Finally we show all the graphs
plt.show()
