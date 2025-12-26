import pytest

from src.numbersets import Natural, Integer, Rational

# =========================
# Создание и валидация
# =========================

def test_rational_creation():
    r = Rational(Integer(1), Integer(2))
    assert r._num._value == 1
    assert r._den._value == 2


def test_rational_default_denominator():
    r = Rational(Integer(3))
    assert r._num._value == 3
    assert r._den._value == 1


def test_rational_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        Rational(Integer(1), Integer(0))


def test_rational_invalid_types():
    with pytest.raises(TypeError):
        Rational(1, 2)


# =========================
# Нормализация
# =========================

def test_rational_normalization():
    r = Rational(Integer(2), Integer(4))
    assert r._num._value == 1
    assert r._den._value == 2


def test_rational_sign_normalization():
    r = Rational(Integer(-1), Integer(-2))
    assert r._num._value == 1
    assert r._den._value == 2


def test_rational_negative_denominator():
    r = Rational(Integer(1), Integer(-2))
    assert r._num._value == -1
    assert r._den._value == 2


# =========================
# Арифметика
# =========================

def test_rational_add():
    a = Rational(Integer(1), Integer(2))
    b = Rational(Integer(1), Integer(3))
    assert a + b == Rational(Integer(5), Integer(6))


def test_rational_add_integer():
    r = Rational(Integer(1), Integer(2))
    i = Integer(1)
    assert r + i == Rational(Integer(3), Integer(2))


def test_rational_add_natural():
    r = Rational(Integer(1), Integer(2))
    n = Natural(1)
    assert r + n == Rational(Integer(3), Integer(2))


def test_rational_sub():
    a = Rational(Integer(3), Integer(4))
    b = Rational(Integer(1), Integer(4))
    assert a - b == Rational(Integer(1), Integer(2))


def test_rational_mul():
    a = Rational(Integer(2), Integer(3))
    b = Rational(Integer(3), Integer(4))
    assert a * b == Rational(Integer(1), Integer(2))


def test_rational_div():
    a = Rational(Integer(1), Integer(2))
    b = Rational(Integer(3), Integer(4))
    assert a / b == Rational(Integer(2), Integer(3))


# =========================
# Степени
# =========================

def test_rational_pow_positive():
    r = Rational(Integer(2), Integer(3))
    n = Integer(2)
    assert r ** n == Rational(Integer(4), Integer(9))


def test_rational_pow_zero():
    r = Rational(Integer(5), Integer(7))
    n = Integer(0)
    assert r ** n == Rational(Integer(1), Integer(1))


def test_rational_pow_negative():
    r = Rational(Integer(2), Integer(3))
    n = Integer(-1)
    assert r ** n == Rational(Integer(3), Integer(2))


def test_rational_zero_pow_zero():
    r = Rational(Integer(0), Integer(1))
    n = Integer(0)
    with pytest.raises(ValueError):
        r ** n


# =========================
# Сравнения
# =========================

def test_rational_comparisons():
    a = Rational(Integer(1), Integer(2))
    b = Rational(Integer(2), Integer(4))
    c = Rational(Integer(3), Integer(4))

    assert a == b
    assert a < c
    assert c > a
    assert a <= b
    assert c >= b


def test_rational_compare_integer():
    r = Rational(Integer(3), Integer(1))
    i = Integer(3)

    assert r == i
    assert not (r < i)
    assert not (r > i)


def test_rational_compare_natural():
    r = Rational(Integer(5), Integer(1))
    n = Natural(5)

    assert r == n


# =========================
# str и repr
# =========================

def test_rational_str():
    assert str(Rational(Integer(3), Integer(1))) == "3"
    assert str(Rational(Integer(1), Integer(2))) == "1/2"


def test_rational_repr():
    r = Rational(Integer(1), Integer(2))
    assert repr(r) == "Rational(Integer(1), Integer(2))"