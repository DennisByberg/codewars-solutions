import pytest

from human_years_cat_years_dog_years import human_years_cat_years_dog_years


@pytest.mark.parametrize(
    "human,expected",
    [
        (1, [1, 15, 15]),
        (2, [2, 24, 24]),
        (3, [3, 28, 29]),
        (4, [4, 32, 34]),
        (10, [10, 56, 64]),
    ],
)
def test_fixed(human, expected):
    assert human_years_cat_years_dog_years(human) == expected
