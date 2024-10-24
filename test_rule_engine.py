# test_rule_engine.py

from rule_engine import create_rule, evaluate_rule
from database import store_rule, modify_rule, retrieve_rule

def test_user_defined_function():
    rule = "total_user_spend > 50000"
    ast = create_rule(rule)

    data = {"campaign_spend": [20000, 35000, 5000]}
    result = evaluate_rule(ast, data)
    
    assert result == True
    print("User-defined function test passed!")

if __name__ == "__main__":
    test_user_defined_function()

def test_rule_engine():
    # Basic rule creation and evaluation
    rule1 = "age > 30 AND department = 'Sales'"
    ast = create_rule(rule1)
    store_rule(rule1, ast)

    data1 = {"age": 35, "department": "Sales"}
    data2 = {"age": 25, "department": "Marketing"}

    assert evaluate_rule(ast, data1) == True
    assert evaluate_rule(ast, data2) == False
    print("Rule evaluation passed!")

    # Modify the rule
    modify_rule(1, "age > 25 AND department = 'Marketing'")
    modified_ast = retrieve_rule(1)
    
    data3 = {"age": 26, "department": "Marketing"}
    assert evaluate_rule(modified_ast, data3) == True
    print("Rule modification passed!")

def test_invalid_rules():
    try:
        create_rule("age >")
    except ValueError as e:
        assert str(e) == "Invalid comparison: Missing attribute or value"
    
    try:
        create_rule("invalid_attr > 30")
    except ValueError as e:
        assert str(e) == "Invalid attribute: invalid_attr"
    
    print("Invalid rule tests passed!")

if __name__ == "__main__":
    test_rule_engine()
    test_invalid_rules()
