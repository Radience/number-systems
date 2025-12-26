class Natural:
    def __init__(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Натуральное число должно быть целым")
        if value <= 0:
            raise ValueError("Натуральное число должно быть больше нуля")
        self._value = value

    def __add__(self, other: Natural) -> Natural:
        if not isinstance(other, Natural):
            return NotImplemented
        return Natural(self._value + other._value)
    
    def __mul__(self, other: Natural) -> Natural:
        if not isinstance(other, Natural):
            return NotImplemented
        return Natural(self._value * other._value)

    def __pow__(self, other: Natural) -> Natural:
        if not isinstance(other, Natural):
            return NotImplemented
        return Natural(self._value ** other._value)
    
    def __eq__(self, other: Natural) -> bool:
        if not isinstance(other, Natural):
            return NotImplemented
        return self._value == other._value
    
    def __lt__(self, other: Natural) -> bool:
        if not isinstance(other, Natural):
            return NotImplemented
        return self._value < other._value
    
    def __gt__(self, other: Natural) -> bool:
        if not isinstance(other, Natural):
            return NotImplemented
        return self._value > other._value
    
    def __le__(self, other: Natural) -> bool:
        if not isinstance(other, Natural):
            return NotImplemented
        return self._value <= other._value
    
    def __ge__(self, other: Natural) -> bool:
        if not isinstance(other, Natural):
            return NotImplemented
        return self._value >= other._value
    
    def __repr__(self):
        return f'Natural({self._value})'