
# AWS DMS Table Mapping Generator

This python script generates a JSON file for the AWS DMS table mappings section. This script is useful if you work with hundreds and thousands of tables.

Here's a **`Table Mapping Generator`** demo:

![Table Mapping Generator demo GIF](img/table_mapping_generator.gif)

After script run it will create a **table_mapping.json** file in the same directory. That file will look like this.

```json
  {
    "rules": [
        {
            "rule-type": "selection",
            "rule-id": 0,
            "rule-name": 0,
            "object-locator": {
                "schema-name": "dbo",
                "table-name": "table1",
                "table-type": "table"
            },
            "rule-action": "include",
            "filters": []
        },
        {
            "rule-type": "selection",
            "rule-id": 1,
            "rule-name": 1,
            "object-locator": {
                "schema-name": "dbo",
                "table-name": "table2",
                "table-type": "table"
            },
            "rule-action": "include",
            "filters": []
        }
    ]
}
```


## Installation

> This script works with Python3

Clone the repo \
Install requirements \
Run the script

```bash
  git clone https://github.com/emreoztoprak/dms-table-mapping-generator.git
  pip install -r requirements.txt
  ./table_mapping_generator.py
```
    


## Usage

When you run the script it will ask for the file containing the list of tables. That file should be like this.

```
table1
table2
```

After that, it will ask schema name. The default value is a wildcard. You can leave it or enter your schema name. That schema name will be applicable to all tables in the list. 

The last ones are rule action and whether you migrate tables, views, or all.


## More About AWS DMS Table Mapping

If you want to know more about how to configure table mapping you can read this documentation.

[Using table mapping to specify task settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html)


