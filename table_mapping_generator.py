#!/usr/bin/env python3

import json, os, readline
from bullet import Bullet

data = {}
data['rules'] = []

print('\n')
readline.set_completer_delims(' \t\n=')
readline.parse_and_bind("tab: complete")
table_list_input = input("Enter the path of your table list file: ")     
assert os.path.exists(table_list_input), "I did not find the table list file at, " + table_list_input

def readTableList():
    file = open(table_list_input, "r")
    file_lines = file.read()
    list_of_lines = file_lines.split("\n")
    return list_of_lines

print('\n')
schema_list_input = input("Enter the schema name \n(Default value is %) : ") or "%"

def ruleAction():
    rule_action = ["include","exclude","explicit"]
    prompt = Bullet(
            prompt = "\nSelect a action for your rules : ",
            choices = rule_action, 
            indent = 0,
            align = 5, 
            margin = 2,
            shift = 0,
            bullet = "",
            pad_right = 5,
            return_index = False
        )
    selected_profiles = prompt.launch()
    return selected_profiles

rule_action=ruleAction()

def tableType():
    table_types = ["table","view","all"]
    prompt = Bullet(
            prompt = "\nSelect whether to migrate tables, views or all : ",
            choices = table_types, 
            indent = 0,
            align = 5, 
            margin = 2,
            shift = 0,
            bullet = "",
            pad_right = 5,
            return_index = False
        )
    selected_type = prompt.launch()
    return selected_type

table_type=tableType()

def createJSON():
        for i in range(0,len(readTableList())):
            data['rules'].append({
            "rule-type": "selection",
            "rule-id": i,
            "rule-name": i,
            "object-locator": {
                "schema-name": schema_list_input,
                "table-name": readTableList()[i],
                "table-type": table_type
            },
            "rule-action": rule_action,
            "filters": []
            })        
        with open('table_mapping.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
createJSON()
print('\n')
print("It's done. Please check your table_mapping.json file.")