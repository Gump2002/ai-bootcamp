import pytest

from ai_bootcamp.stats import mean, var


def test_mean_basic():
    assert mean([1, 2, 3, 4]) == 2.5


def test_var_basic():
    assert var([1, 2, 3, 4]) == pytest.approx(1.25)


def test_empty_raises():
    with pytest.raises(ValueError):
        mean([])
