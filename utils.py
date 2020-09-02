# -*- coding: utf-8 -*-
import numpy as np


def extract_plot_ranges(X, pad=0.5):
    """Extract plot ranges given 1D arrays of X and Y axis values."""
    min_x1, max_x1 = np.min(X[:, 0]) - pad, np.max(X[:, 0]) + pad
    min_x2, max_x2 = np.min(X[:, 1]) - pad, np.max(X[:, 1]) + pad
    return min_x1, max_x1, min_x2, max_x2


def generate_grid_points(min_x, max_x, min_y, max_y, resolution=100):
    """Generate resolution * resolution points within a given range."""
    xx, yy = np.meshgrid(np.linspace(min_x, max_x, resolution), 
                         np.linspace(min_y, max_y, resolution))
    return np.c_[xx.ravel(), yy.ravel()]
