#encoding = utf-8
import numpy as np

def assert_true(value):
    return np.testing.assert_equal(value, True)

assert_true = assert_true
assert_equal = np.testing.assert_equal
assert_array_equal = np.testing.assert_array_equal
assert_almost_equal = np.testing.assert_almost_equal
