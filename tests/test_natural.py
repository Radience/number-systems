import pytest

from src.numbersets import Natural

def test_natural_creation(): #Корректное создание
    n = Natural(5)
    assert n._value == 5

def test_natural_not_int(): #Ошибка, если не int
    with pytest.raises(TypeError):
        Natural(3.14)

def test_natural_non_positive(): #Ошибка, если ≤ 0
    with pytest.raises(ValueError):
        Natural(0)

    with pytest.raises(ValueError):
        Natural(-3)

def test_natural_add(): #Сложение
    a = Natural(3)
    b = Natural(4)
    c = a + b

    assert isinstance(c, Natural)
    assert c._value == 7

def test_natural_mul(): #умножение
    a = Natural(3)
    b = Natural(5)

    assert (a * b)._value == 15

def test_natural_pow(): #степень
    a = Natural(2)
    b = Natural(3)

    assert (a ** b)._value == 8

def test_natural_comparisons(): #сравнение
    a = Natural(3)
    b = Natural(5)

    assert a < b
    assert b > a
    assert a <= b
    assert b >= a
    assert a != b
    assert a == Natural(3)

def test_natural_abs(): #модуль
    a = Natural(7)
    b = abs(a)

    assert isinstance(b, Natural)
    assert b._value == 7

def test_natural_repr(): #repr
    n = Natural(4)
    assert repr(n) == 'Natural(4)'

def test_natural_str():
    n = Natural(6)
    assert str(n) == '6'