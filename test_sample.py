import prime

# content of test_sample.py
# def inc(x):
#     return x + 1
#
#
# def test_answer():
#     assert inc(3) == 4
#
#
# def test_prime():
#     assert prime.is_prime(3)
#     assert prime.is_prime(5)

import exo11

def test_departements():
    assert exo11.get_dept(41)=="Loir-et-Cher"
    assert exo11.get_dept(91)=="Essonne"
    assert exo11.get_dept(48)=="Lozère"