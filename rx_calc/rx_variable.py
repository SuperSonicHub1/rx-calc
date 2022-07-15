from ast import AST, Name, walk
from typing import TypeVar, List, Dict, Any

from .variable import Variable
from .resolve import resolve_value

T = TypeVar("T")


class RxVariable(Variable[T]):
    def __init__(self, name: str, expr: AST, variables: Dict[str, Variable]) -> None:
        self.expr = expr
        self.variables = variables
        super().__init__(name, self.resolve())
        for var in map(
            lambda name: variables[name.id],
            filter(lambda node: isinstance(node, Name), walk(expr)),
        ):
            var.subscribe(on_next=self.on_change)

    def resolve(self) -> Any:
        return resolve_value(self.variables, self.expr)

    def on_change(self, _):
        # No intelligent partial updating here!
        self.value = self.resolve()
        print(f"Variable {self.name!r} is now: {self.value}")
