from src.math_operations import add, sub
def test_add():
    assert add(3,2)==5
    assert add(1,6)==7
    assert add(0,2)==2
    assert add(-3,6)==3


def test_sub():
    assert sub(3,2)==1
    assert sub(4,-1)==5
    assert sub(1,2)==-1
