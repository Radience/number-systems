from . import Natural

class Integer():
    def __init__(self, value: int | Natural):
        if not isinstance(value, int):
            raise TypeError("Целое число должно быть целым")
        if isinstance(value, Natural):
            self._value = value._value
        self._value = value

    def __add__(self, other: Integer | Natural) -> Integer:
        if not isinstance(other, (Integer, Natural)):
            return NotImplemented
        return Integer(self._value + other._value)
    
    def __sub__(self, other: Integer | Natural) -> Integer:
        if not isinstance(other, (Integer, Natural)):
            return NotImplemented
        return Integer(self._value - other._value)
    
    def __mul__(self, other: Integer | Natural) -> Integer:
        if not isinstance(other, (Integer, Natural)):
            return NotImplemented
        return Integer(self._value * other._value)

    def __pow__(self, other: Integer | Natural) -> Integer:
        if not isinstance(other, (Integer, Natural)):
            return NotImplemented
        if other._value < 0:
            return NotImplemented
        return Integer(self._value ** other._value)
    
    def __eq__(self, other: Integer | Natural) -> bool:
        if not isinstance(other, (Integer, Natural)):
            return NotImplemented
        return self._value == other._value
    
    def __lt__(self, other: Integer | Natural) -> bool:
        if not isinstance(other, (Integer, Natural)):
            return NotImplemented
        return self._value < other._value
    
    def __gt__(self, other: Integer | Natural) -> bool:
        if not isinstance(other, (Integer, Natural)):
            return NotImplemented
        return self._value > other._value
    
    def __le__(self, other: Integer | Natural) -> bool:
        if not isinstance(other, (Integer, Natural)):
            return NotImplemented
        return self._value <= other._value
    
    def __ge__(self, other: Integer | Natural) -> bool:
        if not isinstance(other, (Integer, Natural)):
            return NotImplemented
        return self._value >= other._value
    
    def __abs__(self):
        if self._value >= 0:
            return self
        return Integer(-self._value)
    
    def __repr__(self):
        return f'Integer({self._value})'