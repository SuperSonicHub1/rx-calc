from typing import TypeVar, Tuple
from reactivex.subject import Subject

T = TypeVar("T")


class Variable(Subject[Tuple[str, T]]):
    def __init__(self, name: str, value: T) -> None:
        super().__init__()
        self.name = name
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: T):
        self._value = value
        self.on_next((self.name, value))

    def __repr__(self):
        return f"Variable(name={self.name!r}, value={self.value!r})"

    # Dunder method re-implementations

    def __str__(self):
        return self.value.__str__()

    def __add__(self, other):
        return self.value.__add__(other)

    def __sub__(self, other):
        return self.value.__sub__(other)

    def __mul__(self, other):
        return self.value.__mul__(other)

    def __matmul__(self, other):
        return self.value.__matmul__(other)

    def __truediv__(self, other):
        return self.value.__truediv__(other)

    def __floordiv__(self, other):
        return self.value.__floordiv__(other)

    def __mod__(self, other):
        return self.value.__mod__(other)

    def __divmod__(self, other):
        return self.value.__divmod__(other)

    def __pow__(self, other, modulo=None):
        return self.value.__pow__(other, modulo=modulo)

    def __lshift__(self, other):
        return self.value.__lshift__(other)

    def __rshift__(self, other):
        return self.value.__rshift__(other)

    def __and__(self, other):
        return self.value.__and__(other)

    def __xor__(self, other):
        return self.value.__xor__(other)

    def __or__(self, other):
        return self.value.__or__(other)
