import matplotlib.pyplot as plt
import math
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
# Sample data
x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("(1) x^2  (2) 1/x  (3) sqrt(x)  (4) 1/x  (5) User defined Function\nChoose a Function:  ", end="")
choice = int(input())

graph_name = ""
y_values = [1, 2, 3, 4, 5]
if choice == 1:
    y_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    graph_name = "y = x"
elif choice == 2:
    y_values = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]
    graph_name = "y = x^2"
elif choice == 3:
    y_values = [1, 1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9, 1/10, 1/11, 1/12, 1/13, 1/14, 1/15]
    graph_name = "y = 1/x"
elif choice == 4:
    y_values = [1, math.sqrt(2), math.sqrt(3), math.sqrt(4), math.sqrt(5), math.sqrt(6), math.sqrt(7), math.sqrt(8), math.sqrt(9), math.sqrt(10), math.sqrt(11), math.sqrt(12), math.sqrt(13), math.sqrt(14), math.sqrt(15)]
    graph_name = "y = sqrt(x)"
else:
    x_values = [1, 2, 3, 4, 5]
    for i in range(5):
        print("Enter corresponding y value when x=", i+1, end=" :")
        y_values[i] = int(input())

# Plot the graph
plt.plot(x_values, y_values)

plt.title(graph_name)
plt.grid(True)

# Display the graph
plt.show()

