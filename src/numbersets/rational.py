from __future__ import annotations

from . import Natural, Integer

NumberSet = 'Natural | Integer | Rational'

class Rational:
    def __init__(self, numerator: Integer | Natural, denominator: Integer | Natural = Natural(1)):
        if not isinstance(numerator, (Integer, Natural)):
            raise TypeError('Числитель должен быть целым или натуральным числом')
        if not isinstance(denominator, (Integer, Natural)):
            raise TypeError('Знаменатель должен быть целым или натуральным числом')
        if denominator._value == 0:
            raise ZeroDivisionError('Знаменатель не можеть быть нуль')
        self._num = numerator
        self._den = denominator
        self._normalize()

    @staticmethod
    def _gcd(a: int, b: int):
        while b != 0:
            a, b = b, a % b
        return abs(a)
    
    def _normalize(self):
        g = self._gcd(abs(self._num._value), abs(self._den._value))
        self._num = Integer(self._num._value // g)
        self._den = Integer(self._den._value // g)
        if self._den._value < 0:
            self._num = Integer(-self._num._value)
            self._den = Integer(-self._den._value)

    def __add__(self, other: NumberSet) -> Rational:
        if isinstance(other, (Natural, Integer)):
            other = Rational(other)
        elif not isinstance(other, Rational):
            return NotImplemented
        num = self._num._value * other._den._value + self._den._value * other._num._value
        den = self._den._value * other._den._value
        return Rational(Integer(num), Integer(den))
    
    def __sub__(self, other: NumberSet) -> Rational:
        if isinstance(other, (Natural, Integer)):
            other = Rational(other)
        elif not isinstance(other, Rational):
            return NotImplemented
        num = self._num._value * other._den._value - self._den._value * other._num._value
        den = self._den._value * other._den._value
        return Rational(Integer(num), Integer(den))
    
    def __mul__(self, other: NumberSet) -> Rational:
        if isinstance(other, (Natural, Integer)):
            other = Rational(other)
        elif not isinstance(other, Rational):
            return NotImplemented
        num = self._num._value * other._num._value
        den = self._den._value * other._den._value
        return Rational(Integer(num), Integer(den))

    def __truediv__(self, other: NumberSet) -> Rational:
        if isinstance(other, (Natural, Integer)):
            other = Rational(other)
        elif not isinstance(other, Rational):
            return NotImplemented
        num = self._num._value * other._den._value
        den = self._den._value * other._num._value
        return Rational(Integer(num), Integer(den))

    def __pow__(self, other: Natural | Integer) -> Rational:
        if not isinstance(other, (Natural, Integer)):
            return NotImplemented
        if self._num._value == 0:
            if other._value <= 0:
                raise ValueError('0^0 и 0^-n не определены')
            else:
                return Rational(Integer(0), Integer(1))
        else:
            num = self._num._value ** abs(other._value)
            den = self._den._value ** abs(other._value)
            if other._value == 0:
                return Rational(Integer(1), Integer(1))
            elif other._value < 0:
                return Rational(Integer(den), Integer(num))
            else:
                return Rational(Integer(num), Integer(den))
            
    def _compare_values(self, other: NumberSet, sym_comp: str) -> bool:
        if not isinstance(other, (Natural, Integer, Rational)):
            return NotImplemented
        if isinstance(other, (Natural, Integer)):
            other = Rational(other)
        match(sym_comp):
            case 'eq': #eq
                return self._num * other._den == self._den * other._num
            case 'ne': #ne
                return self._num * other._den != self._den * other._num
            case 'ge': #ge
                return self._num * other._den >= self._den * other._num
            case 'le': #le
                return self._num * other._den <= self._den * other._num
            case 'gt': #gt
                return self._num * other._den > self._den * other._num
            case 'lt': #lt
                return self._num * other._den < self._den * other._num
        return None

    def __eq__(self, other: NumberSet) -> bool:
        return self._compare_values(other, 'eq')
    
    def __ne__(self, other: NumberSet) -> bool:
        return self._compare_values(other, 'ne')

    def __gt__(self, other: NumberSet) -> bool:
        return self._compare_values(other, 'gt')
    
    def __lt__(self, other: NumberSet) -> bool:
        return self._compare_values(other, 'lt')
    
    def __ge__(self, other: NumberSet) -> bool:
        return self._compare_values(other, 'ge')
    
    def __le__(self, other: NumberSet) -> bool:
        return self._compare_values(other, 'le')
        
    def __repr__(self):
        return f'Rational({repr(self._num)}, {repr(self._den)})'

    def __str__(self):
        if self._den._value == 1:
            return str(self._num._value)
        return f'{self._num._value}/{self._den._value}'