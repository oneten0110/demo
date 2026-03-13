import pytest
from a import add
from s import sub

def test_dd():
    assert add(4,3)==7
def test_d():    
    assert sub(4,4)==0
