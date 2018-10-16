from mycalculator import *

def test_addition():
	assert addition(3,4) == 7

def test_subtraction():
	assert subtraction(3,4) == -1

def test_multiply():
	assert multiply(3,4) == 12

def test_divide():
	assert divide(6,3) == 2

def test_average():
	assert average(3,3,3,3) == 3