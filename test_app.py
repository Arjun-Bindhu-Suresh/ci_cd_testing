import pytest
from app import calculate_area

# Existing test
def test_calculate_area():
    assert calculate_area(4) == 16

# New test using your student ID (100990351 -> Last two digits: 51)
def test_calculate_area_student_id():
    assert calculate_area(51) == 2601  # Correct expected output


