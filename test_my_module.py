from my_module import add, divide
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide():
    assert divide(6, 3) == 2.0
    with pytest.raises(ValueError):
        divide(5, 0)

        
