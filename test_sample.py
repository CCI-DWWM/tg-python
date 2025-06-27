import prime

# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4


def test_prime():
    assert prime.is_prime(3)
    assert prime.is_prime(5)
    assert prime.is_prime(8)
    assert prime.is_prime(6)
    assert prime.is_prime(7)
    assert prime.is_prime(9)
