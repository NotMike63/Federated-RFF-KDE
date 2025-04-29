import numpy as np
import pandas as pd

def gaussian_kernel(h, x, y):
    delta_inner = np.power((x - y), 2)
    delta = np.abs(delta_inner)
    euler_inner = -1 * (np.power(delta, 2)) / (2 * h * h)
    np.exp(euler_inner)

# Computes the gaussian KDE across set given point
def gaussian_kde(d_i, dataset):

    for row in dataset.rows:
        for column in dataset.columns:
            gaussian_kernel(d_i)



# Derivation of the Gaussian Kernel
def random_fourier_features(x, y):
    gaussian_kernel(h, x, y)