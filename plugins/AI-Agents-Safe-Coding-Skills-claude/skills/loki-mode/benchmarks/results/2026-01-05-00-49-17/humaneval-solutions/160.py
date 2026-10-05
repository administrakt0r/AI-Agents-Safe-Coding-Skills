import ast
import operator as op_module

OPERATORS = {
    ast.Add: op_module.add,
    ast.Sub: op_module.sub,
    ast.Mult: op_module.mul,
    ast.FloorDiv: op_module.floordiv,
    ast.Pow: op_module.pow,
    ast.USub: op_module.neg,
    ast.UAdd: op_module.pos,
}

def safe_eval(expr_str):
    node = ast.parse(expr_str, mode='eval')
    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        elif isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError('Invalid constant type')
        elif isinstance(node, ast.BinOp):
            left = _eval(node.left)
            right = _eval(node.right)
            op_type = type(node.op)
            if op_type in OPERATORS:
                return OPERATORS[op_type](left, right)
            raise ValueError(f'Unsupported binary operator: {op_type}')
        elif isinstance(node, ast.UnaryOp):
            operand = _eval(node.operand)
            op_type = type(node.op)
            if op_type in OPERATORS:
                return OPERATORS[op_type](operand)
            raise ValueError(f'Unsupported unary operator: {op_type}')
        else:
            raise ValueError(f'Unsupported node type: {type(node)}')
    return _eval(node)


def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """
    expression = str(operand[0])
    for i, op in enumerate(operator):
        expression += ' ' + op + ' ' + str(operand[i + 1])
    return safe_eval(expression)
