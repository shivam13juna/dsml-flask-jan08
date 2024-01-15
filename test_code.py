from app import sum_something, sub_something, mul_something



def test_sum_something():
    a, b = 1, 2

    assert sum_something(a, b) == 3


def test_sub_something():
    a, b = 1, 2

    assert sub_something(a, b) == -1
    



def test_mul_something():
    a, b = 1, 2

    assert mul_something(a, b) == 2

