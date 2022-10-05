import pytest
from src.calctriangulo import triangle_type

def test_1(): 
        assert triangle_type(12,45,32) == "Not a triangle"
       
def test_2(): 
        assert triangle_type(9,9,9) == "Equilateral"

def test_3(): 
        assert triangle_type(15,15,25) == "Isosceles"

def test_4(): 
        assert triangle_type(20,15,10) == "Scalene"







    
