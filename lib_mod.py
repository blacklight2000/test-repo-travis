# module lib_mod

def mult(n1,n2):
    return n1 * n2

def add(n1,n2):
    return n1 + n2

def substract(n1,n2):
    return n1 - n2

def test_mult_3_4():
    assert(mult(3,4) == 12)

def test_add_3_4():
    assert(add(3,4) ==7)

def test_substract_3_4():
    assert(substract(3,4) == -1)

