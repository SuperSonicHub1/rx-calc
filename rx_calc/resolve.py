from ast import (
	dump,
	AST,
	Sub,
	Mult,
	Div,
	FloorDiv,
	Mod,
	Pow,
	LShift,
	RShift,
	BitOr,
	BitXor,
	BitAnd,
	MatMult,
	Add,
	BinOp,
	Constant,
	Name,
	UAdd,
	USub,
	Not,
	Invert,
	UnaryOp,
)
from decimal import Decimal
import operator
from typing import Any, Dict
from .exception import RxException
from .variable import Variable

binary_operator_to_function = {
	Add: operator.add,
	Sub: operator.sub,
	Mult: operator.mul,
	Div: operator.truediv,
	FloorDiv: operator.floordiv,
	Mod: operator.mod,
	Pow: operator.pow,
	LShift: operator.lshift,
	RShift: operator.rshift,
	BitOr: operator.or_,
	BitXor: operator.xor,
	BitAnd: operator.and_,
	MatMult: operator.matmul,
}

unary_operator_to_function = {
	UAdd: operator.pos,
	USub: operator.neg,
	Not: operator.not_,
	Invert: operator.invert,
}

def resolve_value(variables: Dict[str, Variable], value: AST) -> Any:
	if type(value) == Constant:
		value_value = value.value
		if isinstance(value, (int, float)):
			return Decimal(value)
		else:
			return value_value
	elif type(value) == Name:
		if value.id in variables:
			return variables[value.id].value
		else:
			raise RxException(f"Variable does not exist: {value.id}", )
	elif type(value) == BinOp:
		return binary_operator_to_function[type(value.op)](
			resolve_value(variables, value.left),
			resolve_value(variables, value.right)
		)
	elif type(value) == UnaryOp:
		return unary_operator_to_function[type(value.op)](
			resolve_value(variables, value.operand),
		)
	else:
		raise RxException(f"Unsupported value type: {dump(value)}")
