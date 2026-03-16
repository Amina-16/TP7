import sys
from pathlib import Path

sys.path.insert(0, str(Path(_file_).resolve().parents[1]))
from app.calculator import addition, multiplication

def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0  
    
def test_multiplication():
    assert multiplication(2, 3) == 6
    assert multiplication(-1, 1) == -1
    assert multiplication(0, 5) == 0    
    
