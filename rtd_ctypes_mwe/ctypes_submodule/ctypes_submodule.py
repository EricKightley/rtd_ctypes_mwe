# File ctypes_submodule.py

import os
import numpy as np
from numpy.ctypeslib import ndpointer
import ctypes as ct
import glob

path = os.path.abspath(__file__)
path = os.path.realpath(path)
path = os.path.dirname(path)
path = glob.glob(path + '/_ctypes_submodule*.so')[0]
_ctypes_submodule = ct.CDLL(path)

_ctypes_submodule.add_vectors.restype = None
_ctypes_submodule.add_vectors.argtypes = [
    ndpointer(ct.c_double, flags='C_CONTIGUOUS'),
    ndpointer(ct.c_double, flags='C_CONTIGUOUS'),
    ndpointer(ct.c_double, flags='C_CONTIGUOUS'),
    ct.c_int
]

def add_vectors(vec1, vec2):
    """
    Add two vectors.

    This function adds two floating-point vectors together.

    :param vec1: the first vector
    :param vec2: the second vector
    :type arg1: nd.array, float
    :type arg2: nd.array, float
    :returns: vec1 + vec2
    :rtype: nd.array, float
    """
    length = len(vec1)
    result = np.zeros(length)
    _ctypes_submodule.add_vectors(result, vec1, vec2, length)
    return result
