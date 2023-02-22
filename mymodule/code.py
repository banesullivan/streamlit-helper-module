"""Module of helper methods."""
import numpy as np


def math_it_up(*args, **kwargs):
    return np.log(*args, **kwargs)


def make_data():
    return np.random.normal(1, 1, size=100)
