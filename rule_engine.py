from rule_parser import parse_rule
from ast_node import Node

def create_rule(rule_string):
    """Create a rule by parsing the rule string and returning the AST."""
    ast = parse_rule(rule_string)
    if not ast or not isinstance(ast, Node):
        raise ValueError("Invalid rule structure.")
    return ast

def evaluate_rule(ast, data):
    if ast.node_type == 'operator':
        if ast.value == 'AND':
            return evaluate_rule(ast.left, data) and evaluate_rule(ast.right, data)
        elif ast.value == 'OR':
            return evaluate_rule(ast.left, data) or evaluate_rule(ast.right, data)
    elif ast.node_type == 'operand':
        attribute, operator, value = parse_condition(ast.value)
        return compare(data.get(attribute), operator, value)
    return False
