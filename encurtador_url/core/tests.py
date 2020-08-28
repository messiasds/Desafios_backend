import pytest

def teste1():

    assert 2==2
    
def teste2():

    with pytest.raises(ZeroDivisionError):
        1/0
