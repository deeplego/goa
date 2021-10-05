from goa import problems

import numpy as np


def test_rastrigin():
    f = problems.Rastrigin()
    num_points = 5
    xbounds, ybounds = f.bounds[0], f.bounds[1]
    x = np.linspace(min(xbounds), max(xbounds), num_points)
    y = np.linspace(min(ybounds), max(ybounds), num_points)
    X, Y = np.meshgrid(x, y)
    grid = np.stack((X.flatten(), Y.flatten()), axis=-1)
    expected = np.asarray(
        [
            f(np.asarray([-5.12, -5.12])),
            f(np.asarray([-2.56, -5.12])),
            f(np.asarray([0.0, -5.12])),
            f(np.asarray([2.56, -5.12])),
            f(np.asarray([5.12, -5.12])),
            f(np.asarray([-5.12, -2.56])),
            f(np.asarray([-2.56, -2.56])),
            f(np.asarray([0.0, -2.56])),
            f(np.asarray([2.56, -2.56])),
            f(np.asarray([5.12, -2.56])),
            f(np.asarray([-5.12, 0.0])),
            f(np.asarray([-2.56, 0.0])),
            f(np.asarray([0.0, 0.0])),
            f(np.asarray([2.56, 0.0])),
            f(np.asarray([5.12, 0.0])),
            f(np.asarray([-5.12, 2.56])),
            f(np.asarray([-2.56, 2.56])),
            f(np.asarray([0.0, 2.56])),
            f(np.asarray([2.56, 2.56])),
            f(np.asarray([5.12, 2.56])),
            f(np.asarray([-5.12, 5.12])),
            f(np.asarray([-2.56, 5.12])),
            f(np.asarray([0.0, 5.12])),
            f(np.asarray([2.56, 5.12])),
            f(np.asarray([5.12, 5.12])),
        ]
    )
    actual = np.apply_along_axis(f, 1, grid)
    assert np.allclose(expected, actual)


def test_ackley():
    f = problems.Ackley()
    num_points = 5
    xbounds, ybounds = f.bounds[0], f.bounds[1]
    x = np.linspace(min(xbounds), max(xbounds), num_points)
    y = np.linspace(min(ybounds), max(ybounds), num_points)
    X, Y = np.meshgrid(x, y)
    grid = np.stack((X.flatten(), Y.flatten()), axis=-1)
    expected = np.asarray(
        [
            f(np.asarray([-32.768, -32.768])),
            f(np.asarray([-16.384, -32.768])),
            f(np.asarray([0.0, -32.768])),
            f(np.asarray([16.384, -32.768])),
            f(np.asarray([32.768, -32.768])),
            f(np.asarray([-32.768, -16.384])),
            f(np.asarray([-16.384, -16.384])),
            f(np.asarray([0.0, -16.384])),
            f(np.asarray([16.384, -16.384])),
            f(np.asarray([32.768, -16.384])),
            f(np.asarray([-32.768, 0.0])),
            f(np.asarray([-16.384, 0.0])),
            f(np.asarray([0.0, 0.0])),
            f(np.asarray([16.384, 0.0])),
            f(np.asarray([32.768, 0.0])),
            f(np.asarray([-32.768, 16.384])),
            f(np.asarray([-16.384, 16.384])),
            f(np.asarray([0.0, 16.384])),
            f(np.asarray([16.384, 16.384])),
            f(np.asarray([32.768, 16.384])),
            f(np.asarray([-32.768, 32.768])),
            f(np.asarray([-16.384, 32.768])),
            f(np.asarray([0.0, 32.768])),
            f(np.asarray([16.384, 32.768])),
            f(np.asarray([32.768, 32.768])),
        ]
    )
    actual = np.apply_along_axis(f, 1, grid)
    assert np.allclose(expected, actual)
