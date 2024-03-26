# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 17:33:24 2023

@author: Paul
"""

import numpy as np
import matplotlib.pyplot as plt

def plot_beta_dist():
    alpha = [1, 5, 10]
    beta_values = [1, 2, 5, 10, 20]
    x = np.linspace(0, 1, 1000)

    for a in alpha:
        for b in beta_values:
            y = x**(a-1) * (1-x)**(b-1)
            y /= np.trapz(y, x)  
            plt.plot(x, y, label=r'$\alpha$ = {}, $\beta$ = {}'.format(a, b))

    plt.title('Beta Distribution')
    plt.xlabel('x')
    plt.ylabel('pdf')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    plot_beta_dist()

