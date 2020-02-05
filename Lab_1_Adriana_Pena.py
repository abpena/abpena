#Adriana Pena
# created Feb 1 2020
# Instructor: Olac Fuentes
# Lab 1
import numpy as np
import matplotlib.pyplot as plt
import math


def circle(center, rad):
    n = int(4 * rad * math.pi) #size of the circle calculated
    t = np.linspace(0, 6.3, n)
    x = center[0] + rad * np.sin(t)
    y = center[1] + rad * np.cos(t) # center of circle being calculated
    return x, y


def draw_circles(ax, n, center, radius):
    if n > 0:
        x, y = circle(center, radius)
        ax.plot(x, y, linewidth=0.5, color='k')
        draw_circles(ax, n - 1, [center[0],center[1]], radius)
        draw_circles(ax, n-1, [center[0], center[1]], radius - 10 *n)
        draw_circles(ax, n - 1, [center[0], center[1]], radius - 10 * n)
        # in the recursive method the concept is to subtract one which will make the circle smaller each time


def squares(ax, n, dx, dy, r):
    if n > 0:
        x1 = dx - r
        y1 = dy + r
        x2 = dx + r
        y2 = dy - r
        p = np.array([[x1, y2], [x1, y1], [x2, y1], [x2, y2], [x1, y2]])
        # ploting where the square will be placed such as your x and y
        ax.plot(p[:, 0], p[:, 1], color='k')
        # recursive calls subtracting one to make more each time
        # the radius would be the width of square
        squares(ax, n - 1, x1, y1, r * .6)
        squares(ax, n - 1, x1, y1, r * .6)
        squares(ax, n - 1, x1, y1, r * .6)
        squares(ax, n - 1, x1, y1, r * .6)
        squares(ax, n - 1, x1, y1, r * .6)


def trees(ax, n, Xc, Yc, x, y):
    if n > 0:
        right = np.array([[x, y], [x - Xc, y - Yc]])
        left = np.array([[x, y], [x + Xc, y - Yc]])
        ax.plot(right[:, 0], right[:, 1], color='k')
        ax.plot(left[:, 0], left[:, 1], color='k')
        trees(ax, n-1, Xc / 2, Yc, x - Xc, y - Yc)
        trees(ax, n-1, Xc / 2, Yc, x - Xc, y - Xc)
        trees(ax, n - 1, Xc / 2, Yc, x - Xc, y - Xc)
        trees(ax, n - 1, Xc / 2, Yc, x - Xc, y - Xc)
        # leaves will be divited by 2 to split branches


def triangle(ax, n, p):
    if n > 0:
        ax.plot(p[:, 0], p[:, 1], linewidth=0.5, color='k')
        il = [1, 2, 3, 1]
        q = p / 2 + p[il] / 2  # constructing the inside triangle
        triangle(ax, n - 1, q)


def triangle_2(ax, n, p):
    if n > 0:
        ax.plot(p[:, 0], p[:, 1], linewidth=0.5, color='k')
        il = [1, 2, 3, 1]
        q = p / 2 + p[il] / 2
        triangle_2(ax, n - 1, q / 2)
        triangle_2(ax, n - 1, q / 2)


if __name__ == "__main__":
    plt.close("all")
    fig, ax = plt.subplots()
    n = 3
    draw_circles(ax, n, [0, 0], 100)
    ax.set_aspect(1.0)
    ax.axis('on')
    plt.show()
    fig.savefig('Circles.png')
    '''
    figure change n:
        n = 3 
        n = 4
    '''

    plt.close("all")
    fig, ax = plt.subplots()
    n = 4
    squares(ax, n, 0, 0, 100)
    ax.set_aspect(1.0)
    ax.axis('on')
    plt.show()
    fig.savefig('squares.png')
    '''
    change n:
        n = 2
        n = 3
        n = 4 
    '''
    plt.close("all")
    fig, ax = plt.subplots()
    n = 2
    ax.axis('on')
    trees(ax,n,100,50,0,0)
    #n change how many times the method is been call,size of the tree/brakets ,size of graph
    ax.set_aspect(1.5) # scale of tree
    plt.show()
    fig.savefig('Tree.png')
    '''
    change n 
    n = 2
    n = 3
    n = 4
    '''

    plt.close("all")
    orig_size = 1000.0
    n = 3
    p = np.array([[0, 0], [500.0, orig_size], [orig_size, 0], [0, 0]])
    fig, ax = plt.subplots()
    ax.axis('on')
    triangle(ax, n, p)
    ax.set_aspect(1.0)
    plt.show()
    fig.savefig('Triangle.png')
    '''
    change n:
        n = 1
        n = 2
        n = 3
    '''
    plt.close("all")
    orig_size = 1000.0
    n = 5
    p = np.array([[0, 0], [500.0, orig_size], [orig_size, 0], [0, 0]])
    fig, ax = plt.subplots()
    ax.axis('on')
    triangle_2(ax, n, p)
    ax.set_aspect(1.0)
    plt.show()
