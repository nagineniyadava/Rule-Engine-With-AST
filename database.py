import sqlite3
import json
from rule_engine import create_rule

# Connect to the SQLite database
conn = sqlite3.connect('rules.db', check_same_thread=False)
cursor = conn.cursor()

# Create the rules table if it doesn't exist
def create_rules_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rule_string TEXT NOT NULL,
            ast_json TEXT NOT NULL
        )
    ''')
    conn.commit()

create_rules_table()

# Store a new rule in the database
def store_rule(rule_string, ast):
    ast_json = json.dumps(ast.to_dict())
    cursor.execute("INSERT INTO rules (rule_string, ast_json) VALUES (?, ?)", (rule_string, ast_json))
    conn.commit()

# Retrieve all rules from the database
def get_all_rules():
    cursor.execute("SELECT id, rule_string FROM rules")
    return {row[0]: row[1] for row in cursor.fetchall()}

# Modify an existing rule by its ID
def modify_rule(rule_id, new_rule_string):
    new_ast = create_rule(new_rule_string)
    ast_json = json.dumps(new_ast.to_dict())
    cursor.execute("UPDATE rules SET rule_string = ?, ast_json = ? WHERE id = ?", (new_rule_string, ast_json, rule_id))
    conn.commit()
    return cursor.rowcount > 0

# Delete a rule by its ID
def delete_rule(rule_id):
    cursor.execute("DELETE FROM rules WHERE id = ?", (rule_id,))
    conn.commit()
    return cursor.rowcount > 0

# Reset (delete) all rules from the database
def reset_rules():
    cursor.execute("DELETE FROM rules")
    conn.commit()
