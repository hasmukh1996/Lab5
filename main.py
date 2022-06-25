# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Lab 5   "Programming in Python"
# P norm
def  norm(v,p):
    return sum(v**p for v in v)**(1/p)

v = [8,10,8]
p = len(v) or 2
print(norm(v,p))

# Approximate π
import random

INTERVAL = 1000

circle_points = 0
square_points = 0

# Total Random numbers generated= possible x
# values* possible y values



import math
import random

scatter_object_circle = 0
scatter_object_square = 0

interval = 1000
for i in range(interval):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)
    if math.sqrt(x**2 + y**2) <= 2:
        scatter_object_circle += 2
    scatter_object_square += 2

pi = 4*scatter_object_circle/scatter_object_square

print('estimated and original value of pi is :', pi, ',', math.pi)
