from ast_node import Node

def parse_rule(rule_string):
    """Parse a rule string and create an AST."""
    if 'AND' in rule_string:
        left_rule, right_rule = rule_string.split('AND', 1)
        return Node(node_type='operator', left=parse_rule(left_rule.strip()), right=parse_rule(right_rule.strip()), value='AND')
    elif 'OR' in rule_string:
        left_rule, right_rule = rule_string.split('OR', 1)
        return Node(node_type='operator', left=parse_rule(left_rule.strip()), right=parse_rule(right_rule.strip()), value='OR')
    elif '>' in rule_string or '<' in rule_string or '=' in rule_string:
        return Node(node_type='operand', value=rule_string.strip())
    raise ValueError("Invalid rule format: Unsupported condition or missing operators.")
