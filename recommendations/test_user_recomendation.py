import pytest

from recommendations.user_recomendation import calculate_score


def test_calculate_score_no_negative():
    assert calculate_score(1, 100) >= 0


def test_calculate_score_no_greatter_than_100():
    assert calculate_score(1, 100) < 100


def test_calculate_score_0_when_user_no_exist():
    assert calculate_score(100, 0) == 0


@pytest.mark.parametrize("a, b, expected",
                         [
                             (1, 20, 19),
                             (1, 21, 19),
                             (1, 22, 19),
                             (1, 23, 23),
                             (1, 24, 23),
                             (1, 25, 23),
                             (2, 20, 19),
                             (2, 21, 19),
                             (2, 22, 19),
                             (2, 23, 23),
                             (2, 24, 23),
                             (2, 25, 23),
                             (3, 20, 19),
                             (3, 21, 19),
                             (3, 22, 19),
                             (3, 23, 23),
                             (3, 24, 23),
                             (3, 25, 23),
                             (4, 20, 19),
                             (4, 21, 19),
                             (4, 22, 19),
                             (4, 23, 23),
                             (4, 24, 23),
                             (4, 25, 23),
                             (5, 20, 19),
                             (5, 21, 19),
                             (5, 22, 19),
                             (5, 23, 23),
                             (5, 24, 23),
                             (5, 25, 23)
                         ], )
def test_addition(a, b, expected):
    assert calculate_score(a, b) == expected
