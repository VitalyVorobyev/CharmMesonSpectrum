from average import average

import numpy as np

def make_data(*args):
    return [
        {'value': v, 'stat': st, 'syst': sy} for v, st, sy in args
    ]

def test_single_result():
    data = make_data([1, 0.03, 0.04])
    expected = (1, 0.05, 0, 1)
    assert expected == average(data)

def test_same_result():
    data = make_data(
        [1, 0.03, 0.0],
        [1, 0.03, 0.0],
    )
    expected = (1, 0.03 / np.sqrt(2), 0, 0)
    assert np.allclose(expected, average(data))
