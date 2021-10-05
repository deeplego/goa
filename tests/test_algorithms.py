import numpy as np

from goa import algorithms


def test_first_stopping_rule_true():
    X = np.array([[0, 0], [2 * np.pi, 0]])
    f = lambda x: np.cos(np.sum(x))
    y = np.apply_along_axis(f, 1, X)
    stopping_rule = algorithms.StoppingRule()
    actual = stopping_rule(y)
    expected = True
    assert expected == actual


def test_first_stopping_rule_false():
    X = np.array([[np.pi, 0], [2 * np.pi, 0]])
    f = lambda x: np.cos(np.sum(x))
    y = np.apply_along_axis(f, 1, X)
    stopping_rule = algorithms.StoppingRule()
    actual = stopping_rule(y)
    expected = False
    assert expected == actual


def test_second_stopping_rule_true_1():
    X1 = np.array([[0, 1, 0.5], [1, 0, -1]])
    X2 = np.array([[0, 1, 0.5], [1, 0, -1]])
    X3 = np.array([[0, 1, 0.5], [1, 0, -1]])
    X4 = np.array([[0, 1, 0.5], [1, 0, -1]])
    all_X = [X1, X2, X3, X4]
    f = lambda x: np.cos(np.sum(x))
    all_y = [np.apply_along_axis(f, 1, X) for X in all_X]
    stopping_rule = algorithms.StoppingRule(max_iterations_without_improvement=2)
    expected = [False, False, True, True]
    actual = [stopping_rule(y) for y in all_y]
    assert np.array_equal(expected, actual)


def test_second_stopping_rule_true_2():
    X1 = np.array([[0, 1, 0.5], [1, 0, 0]])
    X2 = np.array([[0, 1, 0.5], [1, 0, -1]])
    X3 = np.array([[0, 1, 0.5], [1, 0, -1]])
    X4 = np.array([[0, 1, 0.5], [1, 0, -1]])
    all_X = [X1, X2, X3, X4]
    f = lambda x: np.cos(np.sum(x))
    all_y = [np.apply_along_axis(f, 1, X) for X in all_X]
    stopping_rule = algorithms.StoppingRule(max_iterations_without_improvement=2)
    expected = [False, False, False, True]
    actual = [stopping_rule(y) for y in all_y]
    assert np.array_equal(expected, actual)


def test_coordinate_descent_1():
    actual = algorithms.coordinate_method(
        problem=lambda x: (x - 16) ** 2,
        x0=11,
        alpha0=1.0,
        theta=0.5,
        epsilon=1e-2,
        max_iterations=200,
    )
    expected = np.asarray([16.0])
    assert actual in expected


def test_coordinate_descent_2():
    actual = algorithms.coordinate_method(
        problem=lambda x: x ** 2 - 16,
        x0=11,
        alpha0=1.0,
        theta=0.5,
        epsilon=1e-2,
        max_iterations=200,
    )
    expected = np.asarray([0.0])
    assert actual in expected
