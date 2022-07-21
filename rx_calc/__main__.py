from ast import (
	parse,


	AST,
	Assign,
	AugAssign,
	AnnAssign,
	BinOp,
	Expr,
	Module,
	Name,
)
from decimal import Decimal
from traceback import print_exception
import readline
from typing import Dict, Any

from .exception import RxException
from .resolve import resolve_value
from .rx_variable import RxVariable
from .variable import Variable

# Line editing and autocompletion
# python -c "import rlcompleter, readline; print(readline.get_completer_delims())"
completer_delims = ' \t\n`~!@#$%^&*()-=+[{]}\\|;:\'",<>/?'
readline.set_completer_delims(completer_delims)

variable_index = 0

def completer(text, state):
	if state == 0:
		variable_index = 0

	variable_names = list(variables.keys())
	while variable_index < len(variable_names):
		variable_name = variable_names[variable_index]
		variable_index += 1
		if len(text) > 0 and variable_name.startswith(text):
			return variable_name

	return None

readline.set_completer(completer)
readline.parse_and_bind("tab: complete")

variables: Dict[str, Variable] = {
	'inf': Variable('inf', Decimal('Infinity'))
}

stmt_index = 0

def handle_statement(statement: AST):
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
	elif type(statement) == AugAssign:
		target = statement.target
		assert isinstance(target, Name)
		if target.id in variables:
			handle_statement(
				Assign(
					targets=[target],
					value=BinOp(
						left=target,
						op=statement.op,
						right=statement.value
					)
				)
			)
		else:
			raise RxException(f"Variable does not exist: {target.id}")
	else:
		raise RxException(f"Unsupported statement type: statement")

while True:
	try:
		command = input("> ").strip()
		
		# Special commands
		if command.startswith(".exit"):
			exit()

		module: Module = parse(command, f"stmt_{stmt_index}")
		for statement in module.body:
			handle_statement(statement)
	except Exception as e:
		# TODO: Better printing of SyntaxErrors
		if isinstance(e, RxException):
			print(e.args[0])
		else:
			print_exception(e)

	stmt_index += 1
