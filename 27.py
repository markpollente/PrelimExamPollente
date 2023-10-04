import math

def test_gradepassed():
    grade = 50
    assert grade >= 50

def test_conversion():
    celcius = 30
    fahrenheit = 100
    assert celcius + 70 == fahrenheit

def test_area():
    area = 16
    l = 4
    w = 4
    assert l * w == area
