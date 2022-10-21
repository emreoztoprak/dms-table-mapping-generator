#!/usr/bin/env python3

import json
import os
import readline

data = {"rules": []}


def readList(table_list_input):
    lists_of_tables = []
    lists_of_columns = []
    lists_of_rule_action = []
    lists_of_transformed_data_type = []
    lists_of_new_column_name = []
    file = open(table_list_input, "r")
    file_lines = file.read()
    list_of_lines = file_lines.split("\n")
    for lines in list_of_lines:
        property = []
        property = lines.split(",")

        try:
            lists_of_tables.append(property[0])
            lists_of_columns.append(property[1])
            lists_of_rule_action.append(property[2])
            if property[2] == "add-column":
                lists_of_transformed_data_type.append(property[3])
                lists_of_new_column_name.append(" ")
            elif property[2] == "rename":
                lists_of_transformed_data_type.append(" ")
                lists_of_new_column_name.append(property[3])
            elif property[2] == "remove-column":
                lists_of_transformed_data_type.append(" ")
                lists_of_new_column_name.append(" ")
        except IndexError:
            print("end of file")
            continue
    return (
        list_of_lines,
        lists_of_tables,
        lists_of_columns,
        lists_of_rule_action,
        lists_of_transformed_data_type,
        lists_of_new_column_name,
    )


def createJSON(
    schema,
    lists_of_rule_action,
    lists_of_tables,
    lists_of_transformed_data_type,
    lists_of_new_column_name,
    file_path,
    lists_of_columns,
):

    data["rules"].append(
        {
            "rule-type": "selection",
            "rule-id": 100000,
            "rule-name": 100000,
            "object-locator": {"schema-name": schema, "table-name": "%"},
            "rule-action": "include",
            "filters": [],
        }
    )

    for i in range(0, len(readList(file_path)) - 1):
        if lists_of_rule_action[i] == "add-column":
            data["rules"].append(
                {
                    "rule-type": "transformation",
                    "rule-id": i,
                    "rule-name": i,
                    "object-locator": {
                        "schema-name": schema,
                        "table-name": lists_of_tables[i],
                    },
                    "rule-action": lists_of_rule_action[i],
                    "value": f"{lists_of_columns[i]}_hashed",
                    "expression": f"hash_sha256({lists_of_columns[i]})",
                    "data-type": {
                        "type": lists_of_transformed_data_type[i],
                        "length": 65,
                    },
                }
            )
        elif lists_of_rule_action[i] == "rename":
            data["rules"].append(
                {
                    "rule-type": "transformation",
                    "rule-id": i,
                    "rule-name": i,
                    "object-locator": {
                        "schema-name": schema,
                        "table-name": lists_of_tables[i],
                        "column-name": lists_of_columns[i],
                    },
                    "rule-action": lists_of_rule_action[i],
                    "value": lists_of_new_column_name[i],
                }
            )
        elif lists_of_rule_action[i] == "remove-column":
            data["rules"].append(
                {
                    "rule-type": "transformation",
                    "rule-id": i,
                    "rule-name": i,
                    "object-locator": {
                        "schema-name": schema,
                        "table-name": lists_of_tables[i],
                        "column-name": lists_of_columns[i],
                    },
                    "rule-action": lists_of_rule_action[i],
                }
            )
    with open("table_mapping.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    print("\n")
    readline.set_completer_delims(" \t\n=")
    readline.parse_and_bind("tab: complete")
    file_path = input("Enter the path of your table list file: ")
    assert os.path.exists(file_path), "I did not find the table list file at, " + file_path
    print("\n")
    schema = input("Enter the schema name \n : ")
    (
        list_of_lines,
        lists_of_tables,
        lists_of_columns,
        lists_of_rule_action,
        lists_of_transformed_data_type,
        lists_of_new_column_name,
    ) = readList(file_path)

    createJSON(
        schema,
        lists_of_rule_action,
        lists_of_tables,
        lists_of_transformed_data_type,
        lists_of_new_column_name,
        file_path,
        lists_of_columns,
    )
    print("\n")
    print("It's done. Please check your table_mapping.json file.")
