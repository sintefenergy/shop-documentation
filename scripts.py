import os
import pandas as pd

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
        with open(f"{object_path}/{object_type}.md", "w") as f:
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
            f.write(f"# {object_type.capitalize()} (object type)\n")
            f.write(f"{description}\n\n")
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
object_attributes = table[table["Object type"] == "{object_type}"].iloc[:, 1:]
itables.show(object_attributes, dom='tlip', column_filters='header')
```\n\n"""
            )

            # for index, arow in object_attributes.iterrows():
            #     attribute_name = arow["Attribute name"]
            #     datatype = arow["Data type"]
            #     io = arow["I/O"]
            #     license = arow["License"]
            #     version = arow["Version added"]
            #     adescription = arow["Description"]
            #     f.write(f"## {attribute_name}\n")
            #     f.write(f"|Description|Value|\n")
            #     f.write("|---|---|\n")
            #     f.write(f"|Data type|{datatype}|\n")
            #     f.write(f"|I/O|{io}|\n")
            #     f.write(f"|License|{license}|\n")
            #     f.write(f"|Version added|{version}|\n\n")
            #     f.write(f"{adescription}\n\n")

