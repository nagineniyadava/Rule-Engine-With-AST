from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from rule_engine import create_rule, evaluate_rule
from combine_rules import combine_rules
from database import store_rule, get_all_rules, modify_rule, delete_rule, reset_rules

app = Flask(__name__)
CORS(app)

# ... (rest of the code remains the same)
# Serve the UI
@app.route('/')
def home():
    return send_from_directory('', 'index.html')

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    data = request.json
    rule = data.get('rule')

    if not rule:
        return jsonify(success=False, message="Rule cannot be empty"), 400

    # Validate rule format before creating
    try:
        parsed_rule = create_rule(rule)
    except ValueError as e:
        return jsonify(success=False, message=f"Invalid rule format: {str(e)}"), 400

    # Check for duplicates in a case-insensitive manner
    existing_rules = get_all_rules()
    for _, existing_rule in existing_rules.items():
        if rule.strip().lower() == existing_rule.strip().lower():
            return jsonify(success=False, exists=True, message="Rule already exists!"), 200

    # Store the rule if it is unique
    store_rule(rule, parsed_rule)
    return jsonify(success=True, message="Rule created successfully!"), 201

@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    data = request.json
    rule1 = data.get('rule1')
    rule2 = data.get('rule2')

    if not rule1 or not rule2:
        return jsonify(success=False, message="Both rules are required"), 400

    # Validate the rules before combining
    try:
        combined_rule = combine_rules([rule1, rule2])
    except ValueError as e:
        return jsonify(success=False, message=f"Invalid rule combination: {str(e)}"), 400

    # Check for duplicates
    existing_rules = get_all_rules()
    if any(combined_rule.strip().lower() == r.strip().lower() for r in existing_rules.values()):
        return jsonify(success=False, exists=True, message="Combined rule already exists!"), 200

    # Store the combined rule
    store_rule(combined_rule, None)
    return jsonify(success=True, message="Rules combined successfully!"), 201

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    data = request.json
    rule = data.get('rule')
    user_data = data.get('user_data')

    if not rule or not user_data:
        return jsonify(success=False, message="Rule and user data are required"), 400

    try:
        # Parse the rule into an AST before evaluation
        parsed_rule = create_rule(rule)
        result = evaluate_rule(parsed_rule, user_data)
        return jsonify(success=True, result=result), 200
    except ValueError as e:
        return jsonify(success=False, message=str(e)), 400

@app.route('/get_all_rules', methods=['GET'])
def get_all_rules_endpoint():
    rules = get_all_rules()
    formatted_rules = [{"id": rule_id, "rule": rule} for rule_id, rule in rules.items()]
    return jsonify(rules=formatted_rules), 200

@app.route('/modify_rule', methods=['PUT'])
def modify_rule_endpoint():
    data = request.json
    rule_id = data.get('rule_id')
    new_rule = data.get('new_rule')

    if not rule_id or not new_rule:
        return jsonify(success=False, message="Rule ID and new rule are required"), 400

    # Validate new rule format before modifying
    try:
        parsed_rule = create_rule(new_rule)
    except ValueError as e:
        return jsonify(success=False, message=f"Invalid rule format: {str(e)}"), 400

    # Modify the rule
    success = modify_rule(rule_id, new_rule)
    if success:
        return jsonify(success=True, message="Rule modified successfully!"), 200
    return jsonify(success=False, message="Rule ID not found"), 404

@app.route('/delete_rule', methods=['DELETE'])
def delete_rule_endpoint():
    data = request.json
    rule_id = data.get('rule_id')

    if not rule_id:
        return jsonify(success=False, message="Rule ID is required"), 400

    success = delete_rule(rule_id)
    if success:
        return jsonify(success=True, message="Rule deleted successfully!"), 200
    return jsonify(success=False, message="Rule ID not found"), 404

@app.route('/reset_rules', methods=['POST'])
def reset_rules_endpoint():
    reset_rules()
    return jsonify(success=True, message="All rules have been reset."), 200

if __name__ == '__main__':
    app.run(debug=True)
