from src.mathOperation import add,sub

def test_add():
    assert add(2,3) == 5
    assert add(5,3) == 8
    assert add(-2,3) == 1
    assert add(-1,1) == 0


def test_sub():
    assert sub(-1,1) == -2
    assert sub(0,1) == -1
    assert sub(-1,-5) == 4
    assert sub(4,2) == 2
