from ast import (
	parse,

	
	Assign,
	AnnAssign,
	Expr,
	Module,
	Name,
)
from decimal import Decimal
from typing import Dict, Any
from .resolve import resolve_value

from .variable import Variable
from .rx_variable import RxVariable

variables: Dict[str, Variable] = {
	'inf': Variable('inf', Decimal('Infinity'))
}

stmt_index = 0

while True:
	command = input("> ").strip()
	
	# Special commands
	if command.startswith(".exit"):
		exit()

	module: Module = parse(command, f"stmt_{stmt_index}")
	for statement in module.body:
		if type(statement) == Assign:
			assert len(statement.targets) == 1
			target = statement.targets[0]
			assert isinstance(target, Name)
			value = resolve_value(variables, statement.value)
			if target.id in variables:
				variables[target.id].value = value
			else:
				variables[target.id] = Variable(target.id, value)
			print(variables[target.id])
		elif type(statement) == AnnAssign:
			target = statement.target
			assert isinstance(target, Name)
			variables[target.id] = RxVariable(target.id, statement.annotation, variables)
			print(variables[target.id])
		elif type(statement) == Expr:
			print(resolve_value(variables, statement.value))
		# TODO: elif type(statement) == AugAssign
		else:
			raise Exception("Unsupported statement type: ", statement)

	stmt_index += 1
