import pytest

from src.numbersets import Natural, Integer

def test_integer_creation_from_int():  #создание int
    i = Integer(5)
    assert i._value == 5

    j = Integer(-3)
    assert j._value == -3

    z = Integer(0)
    assert z._value == 0

def test_integer_not_int(): #Ошибка, если не int
    with pytest.raises(TypeError):
        Integer(3.14)

def test_integer_add(): #Сложение
    a = Integer(3)
    b = Integer(-5)

    c = a + b
    assert isinstance(c, Integer)
    assert c._value == -2

def test_integer_add_natural(): #Сложение с Natural
    a = Integer(-2)
    b = Natural(5)

    c = a + b
    assert isinstance(c, Integer) 
    assert c._value == 3

def test_integer_sub(): #Вычитание
    a = Integer(5)
    b = Integer(8)

    assert (a - b)._value == -3

def test_integer_mul(): #Умножение
    a = Integer(-3)
    b = Integer(4)

    assert (a * b)._value == -12

def test_integer_pow(): #Возведение в степень
    a = Integer(2)
    b = Integer(3)

    assert (a ** b)._value == 8

def test_integer_pow_negative(): #Степень < 0 запрещена
    a = Integer(2)
    b = Integer(-2)

    with pytest.raises(ValueError):
        a ** b

def test_integer_comparisons(): #Сравнения
    a = Integer(3)
    b = Integer(-1)

    assert a > b
    assert b < a
    assert a >= b
    assert b <= a
    assert a != b
    assert a == Integer(3)

def test_integer_abs(): #модуль
    a = Integer(-5)
    b = abs(a)

    assert isinstance(b, Integer)
    assert b._value == 5

def test_integer_str(): #str
    assert str(Integer(5)) == '5'
    assert str(Integer(-3)) == '-3'

def test_integer_repr(): #repr
    assert repr(Integer(7)) == 'Integer(7)'