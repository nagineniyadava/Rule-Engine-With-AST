from rule_engine import evaluate_rule
from combine_rules import combine_rules

def test_combine_rules():
    rule1 = "age > 30 AND department = 'Sales'"
    rule2 = "salary > 50000 OR experience > 5"
    
    combined_ast = combine_rules([rule1, rule2])

    data1 = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
    data2 = {"age": 25, "department": "Marketing", "salary": 45000, "experience": 6}

    assert evaluate_rule(combined_ast, data1) == True
    assert evaluate_rule(combined_ast, data2) == False
    
    print("Combined rule tests passed!")

if __name__ == "__main__":
    test_combine_rules()
