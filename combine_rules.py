# combine_rules.py

from rule_engine import create_rule
from ast_node import Node

def combine_rules(rule_strings, operator="AND"):
    """
    Combine a list of rules into a single AST using the specified operator.
    
    Args:
        rule_strings (list): A list of rule strings.
        operator (str): The logical operator to combine the rules ("AND" or "OR").
    
    Returns:
        Node: The root of the combined AST.
    """
    if not rule_strings:
        raise ValueError("No rules provided for combination.")

    # Create the initial AST from the first rule.
    combined_ast = create_rule(rule_strings[0])

    # Combine subsequent rules.
    for rule_string in rule_strings[1:]:
        new_ast = create_rule(rule_string)
        combined_ast = Node(
            node_type='operator',
            left=combined_ast,
            right=new_ast,
            value=operator  # Use "AND" or "OR"
        )

    return combined_ast
