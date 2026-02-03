import pytest
from sum_str import sum_str


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("4", "5", "9"),
        ("34", "5", "39"),
        ("9", "", "9"),
        ("", "9", "9"),
        ("", "", "0"),
        ("-5", "3", "-2")
    ],
)
def test_sum_str(a, b, expected):
    assert sum_str(a, b) == expected
