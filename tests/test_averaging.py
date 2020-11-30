from average import average

import numpy as np

def make_data(*args):
    return [
        {'value': v, 'stat': st, 'syst': sy} for v, st, sy in args
    ]

def test_single_result():
    data = make_data([1, 0.03, 0.04])
    expected = (1, 0.05, 0, 1)
    assert np.allclose(expected, average(data))

def test_same_result():
    data = make_data(
        [1, 0.03, 0.0],
        [1, 0.03, 0.0],
    )
    expected = (1, 0.03 / np.sqrt(2), 0, 2)
    assert np.allclose(expected, average(data))

    data = make_data(
        [1, 0., 0.03],
        [1, 0., 0.03],
    )
    expected = (1, 0.03 / np.sqrt(2), 0, 2)
    assert np.allclose(expected, average(data))

    data = make_data(
        [1, 0.03, 0.03],
        [1, 0.03, 0.03],
    )
    expected = (1, 0.03, 0, 2)
    assert np.allclose(expected, average(data))

def test_zero_error():
    data = make_data(
        [1, 0.00, 0.00],
        [2, 0.05, 0.00],
    )
    expected = (1, 0.00, 0, 1)
    assert np.allclose(expected, average(data))

def test_tiny_error():
    data = make_data(
        [1, 1.e-7, 0.00],
        [2, 0.05, 0.00],
    )
    expected = (1, 0.00, 400, 2)
    assert np.allclose(expected, average(data), atol=1e-7)
