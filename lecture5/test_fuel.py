from fuel import convert
from fuel import gauge
import pytest

def test_gauge_E():
    assert gauge(1) == "E"

def test_gauge_F():
    assert gauge(99) == "F"

def test_gauge_Z():
    assert gauge(50) == f"{50}%"

def test_convert_zero_div_err():
    with pytest.raises(ZeroDivisionError):
        convert("3/0") 

def test_convert_value_err():
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("X/Y")
