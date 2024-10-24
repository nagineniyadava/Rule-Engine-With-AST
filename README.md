# AST Rule Engine for Zeotap

## Overview
The AST Rule Engine for Zeotap is a three-tier application that allows users to define, store, modify, combine, and evaluate rules based on user attributes such as age, department, salary, and experience. The rules are represented using Abstract Syntax Trees (ASTs) to support complex conditional logic. The project includes a simple UI, backend APIs, and a database to manage and store the rules.

## Features
- **Create Rules**: Define rules using conditions like age, salary, and department.
- **Combine Rules**: Combine two existing rules using `AND` or `OR` operators.
- **Evaluate Rules**: Evaluate a rule against user-provided data to determine if the conditions are met.
- **Modify Rules**: Update existing rules by providing their ID and new rule definition.
- **Delete Rules**: Remove a rule by specifying its ID.
- **Reset Rules**: Clear all stored rules from the database.
- **Display All Rules**: View all stored rules along with their IDs.

## Prerequisites
- **Python 3.7+**: Download Python from [here](https://www.python.org/downloads/).
- **Flask**: Web framework for the server.
- **Flask-CORS**: For handling CORS (Cross-Origin Resource Sharing).
- **SQLite**: Database for storing rules (comes included with Python).

## Installation
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/cybercinogen/ast-rule-engine.git
    cd ast-rule-engine
    ```

2. **Install dependencies**:
    ```bash
    pip install flask flask-cors
    ```

3. **Start the app**:
    ```bash
    python app.py
    ```

4. **Access the UI in your browser**:
    ```
    Go to http://127.0.0.1:5000/
    ```

## Project Structure

## How It Works
- **Create Rules**: Users can enter rules like `age > 30 AND department = 'Sales'` using the UI. The backend parses this rule into an AST and stores it in the SQLite database.
- **Combine Rules**: Combine two rules using logical operators (AND/OR). This creates a new AST representing the combined rule.
- **Evaluate Rules**: Enter user data and select a rule to evaluate if the user data satisfies the conditions of the rule.
- **Modify Rules**: Update existing rules by providing their ID and a new rule definition.
- **Delete and Reset**: Users can delete individual rules by ID or reset the entire rules database.

## Sample Rules
- **Rule 1**: `age > 30 AND department = 'Sales'`
- **Rule 2**: `salary > 50000 OR experience > 5`
- **Rule 3**: `(age < 25 AND department = 'Marketing') OR (age >= 35 AND department = 'Management')`
- **Rule 4**: `age >= 25 AND age <= 40`

## Example Inputs for Testing
**1. Create a Rule**
- **Input**: `age > 30 AND department = 'Sales'`
- **Expected Output**: "Rule created successfully!" or "Rule already exists!"

**2. Combine Rules**
- **Rule 1**: `age > 30`
- **Rule 2**: `salary > 50000`
- **Expected Output**: "Rules combined successfully!" or "Combined rule already exists!"

**3. Evaluate Rule**
- **Rule**: `age > 30 AND department = 'Sales'`
- **User Data**:
  ```json
  {
    "age": 35,
    "department": "Sales",
    "salary": 60000,
    "experience": 3
  }

