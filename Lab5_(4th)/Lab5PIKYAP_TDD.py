from pytest_bdd import scenario, given, when, then
import pytest
from lab1PIKYAP import get_biquadratic_roots

# TDD тест
def test_two_roots():
    assert get_biquadratic_roots(1, 0, -1) == [-1.0, 1.0]

def test_one_root_zero():
    assert get_biquadratic_roots(1, 0, 0) == [0.0]

def test_no_real_roots():
    assert get_biquadratic_roots(1, 0, 1) == []

def test_a_equals_zero():
    assert get_biquadratic_roots(0, 1, 1) == []
    
