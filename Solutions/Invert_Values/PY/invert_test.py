import pytest

from invert import invert


@pytest.mark.parametrize(
    "values, expected",
    [
        ([1, 2, 3, 4, 5], [-1, -2, -3, -4, -5]),
        ([1, -2, 3, -4, 5], [-1, 2, -3, 4, -5]),
        ([], []),
        ([0], [0]),
        ([-1, -2, -3], [1, 2, 3]),
    ],
)
def test_invert(values, expected):
    assert invert(values) == expected
