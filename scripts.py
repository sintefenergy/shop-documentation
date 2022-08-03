import os
import pandas as pd
import yaml

def insert_line_in_file(filename: str):
    with open(filename, "r", encoding="utf8") as f:
        contents = f.readlines()
    if len(contents) > 3:
        if "<html>" in contents[3]:
            contents.insert(4, "  <script>document.domain='sintef.energy';</script>\n")

    with open(filename, "w", encoding="utf8") as f:
        contents = "".join(contents)
        f.write(contents)

def insert_line_in_all_html(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".html") and not file.endswith("macros.html"):
                print(os.path.join(root, file))
                insert_line_in_file(os.path.join(root, file))

def generate_object_descriptions():
    object_table = pd.read_csv('https://shop.sintef.energy/wp-content/uploads/sites/1/2022/04/objects_v14.csv')
    attribute_table = pd.read_csv('https://shop.sintef.energy/wp-content/uploads/sites/1/2021/11/attributes_v14.csv')

    # for object_type in object_table["Object type"]:
    for index, row in object_table.iterrows():
        # Create file <object_type>.md
        object_type = row["Object type"]
        description = row["Description"]
        object_path = "book/objects"
        if not os.path.exists(object_path):
            os.makedirs(object_path)
        with open(f"{object_path}/{object_type}.md", "w") as f, open(f"{object_path}/examples.yaml") as examples:
            f.write("""---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: 'Python 3'
  name: python3
---\n\n"""
            )

            # Write object type description
            f.write(f"({object_type})=\n")
            f.write(f"# {object_type.capitalize()}\n")
            f.write(f"{description}\n\n")

            f.write(
f"""|||
|---|---|
"""
            )
            f.write('|Outputs|')
            if isinstance(row["Legal output connections"], str):
                for i, o in enumerate(row["Legal output connections"].split(',')):
                    if i > 0:
                        f.write(", ")
                    f.write(f'<a href="{o.strip()}.html">{o.strip()}</a>')
            f.write("|\n")
            f.write(f'|License|{row["License"]}|\n')
            f.write(f'|Release version|{row["Version added"]}|\n')
            f.write('\n')

            # List examples
            f.write("## Examples\n")
            example_list = yaml.load(examples, Loader=yaml.FullLoader)
            if object_type in example_list:
                for item in example_list[object_type]:
                    f.write(f"- []({item})\n")
            f.write("\n")

            # Show table with all attributes
            f.write("## Attributes\n")
            f.write(
f"""```{{code-cell}} ipython3
:tags: ['remove-input', 'full-width']

import itables as itables
from itables import init_notebook_mode
init_notebook_mode(all_interactive=True, connected=True)
import pandas as pd
table = pd.read_csv('https://shop.sintef.energy/wp-content/uploads/sites/1/2021/11/attributes_v14.csv')
object_attributes = table[table["Object type"] == "{object_type}"].reset_index().iloc[:, 2:]
for id, row in object_attributes.iterrows():
    row["Description"] = f'<a href="#{{row["Attribute name"].replace("_","-")}}">Description</a>'
itables.show(object_attributes, dom='tlip', column_filters='header')
```\n\n"""
            )

            object_attributes = attribute_table[attribute_table["Object type"] == object_type]
            for id, row in object_attributes.iterrows():
                f.write(f"(doc-{object_type}-{row['Attribute name']})=\n")
                f.write(f'### {row["Attribute name"]}\n')
                f.write(f"{row['Description']}\n\n")
