# File test_add_vectors.py

import unittest
import numpy as np

from ctypes_submodule import add_vectors

class TestRtdCtypesMwe(unittest.TestCase):
    def assertArrayEqual(self, x, y):
        self.assertTrue(np.allclose(x, y, rtol=1e-6))

    def test_add_vectors(self):
        vec1 = np.array([1,2,3], dtype=np.float64)
        vec2 = np.array([5,6,7], dtype=np.float64)
        result = add_vectors(vec1, vec2)
        self.assertArrayEqual(result, vec1+vec2)
