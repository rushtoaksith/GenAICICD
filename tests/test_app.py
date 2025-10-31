# tests/test_app.py
from app.app import calculate_total

def test_calculate_total():
    assert calculate_total([1,2,3]) == 6
    assert calculate_total([]) == 0
