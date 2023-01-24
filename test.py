import pytest
from app.calculator import Calculator

class TestCals:
    def setup(self):
        self.cals = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.cals.multiply(self, 2, 2) == 4

    def setup(self):
        self.cals = Calculator

    def test_division_calculate_correctly(self):
        assert self.cals.division(self, 2, 2) == 1

    def setup(self):
        self.cals = Calculator

    def test_subtraction_calculate_correctly(self):
        assert self.cals.subtraction(self, 2, 2) == 0

    def setup(self):
        self.cals = Calculator

    def test_adding_calculate_correctly(self):
        assert self.cals.adding(self, 2, 2) == 4
