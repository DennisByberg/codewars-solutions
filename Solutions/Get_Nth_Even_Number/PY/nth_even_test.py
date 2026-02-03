import pytest
from nth_even import nth_even


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 0),
        (2, 2),
        (3, 4),
        (100, 198),
        (1_298_734, 2_597_466),
    ],
)
def test_nth_even(n, expected):
    assert nth_even(n) == expected
