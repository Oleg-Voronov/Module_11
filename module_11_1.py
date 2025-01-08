import matplotlib.pyplot as plt
import numpy as np
from random import randint

def example_1():
    NN_ = 10
    lx = [i+1 for i in range(NN_)]
    ly = [randint(1,NN_+1) for i in range(NN_)]
    fig, ax = plt.subplots()                     
    ax.plot(lx, ly)                              
    plt.show()                                   
#----

def example_2():
    x = np.linspace(0, 3, 100)
    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.plot(x, x, label='linear')
    ax.plot(x, x ** 2, label='quadratic')
    ax.plot(x, x ** 3, label='cubic')
    ax.set_xlabel('x label')
    ax.set_ylabel('y label')
    ax.set_title("Simple Plot")
    ax.legend()  # Add a legend.
    plt.show()
#----

def example_3():
    def my_plotter(ax, data1, data2, param_dict):
        out = ax.plot(data1, data2, **param_dict)
        return out
    data1, data2, data3, data4 = np.random.randn(4, 100)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
    my_plotter(ax1, data1, data2, {'marker': 'x'})
    my_plotter(ax2, data3, data4, {'marker': 'o'})
    plt.show()
#----
def example_4():
    fig, ax = plt.subplots(figsize=(5, 2.7))
    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2 * np.pi * t)
    line, = ax.plot(t, s, lw=2)
    ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
                arrowprops=dict(facecolor='black', shrink=0.05))
    ax.set_ylim(-2, 2)
    plt.show()
# ----

if __name__ == '__main__':
    example_1()
    example_2()
    example_3()
    example_4()

