import os
import yaml
import pandas as pd
from jinja2 import Environment, FileSystemLoader
import bibtexparser

env = Environment(loader=FileSystemLoader("templates/"))

object_table = pd.read_csv('https://shop.sintef.energy/wp-content/uploads/sites/1/2022/04/objects_v14.csv')
object_table.columns = [c.replace(' ', '_') for c in object_table.columns]

attribute_table = pd.read_csv('https://shop.sintef.energy/wp-content/uploads/sites/1/2021/11/attributes_v14.csv')
attribute_table.columns = [c.replace(' ', '_') for c in attribute_table.columns]

with open('book/references.bib', encoding="utf8") as bibfile:
    bib_list = bibtexparser.load(bibfile)
bib_table = pd.DataFrame(bib_list.entries)
bib_table = bib_table[['ID', 'author', 'title', 'journal', 'year', 'url', 'doi', 'abstract']].reset_index()

# Render object pages
object_template = env.get_template("object.md")
with open(f"book/doc/objects/cross-references.yaml") as examples:
    example_list = yaml.load(examples, Loader=yaml.FullLoader)
    for index, row in object_table.iterrows():
        object_type = row["Object_type"]

        # Convert object_type object to dict
        obj = row.to_dict()
        if isinstance(row["Legal_output_connections"], str):
            obj['Legal_output_connections'] = [o.strip() for o in obj['Legal_output_connections'].split(',')]
        else:
            obj['Legal_output_connections'] = []
        kwargs = dict()
        kwargs['object'] = obj

        # Get inputs
        inputs = []
        for id, r in object_table.iterrows():
            connections = [o.strip() for o in r['Legal_output_connections'].split(',')] if isinstance(r["Legal_output_connections"], str) else []
            if object_type in connections:
                inputs.append(r["Object_type"])
        kwargs['inputs'] = inputs
        
        # Check for extensive doc
        if os.path.isfile(f"book/doc/objects/{object_type}.md"):
            with open(f"book/doc/objects/{object_type}.md") as doc:
                kwargs['doc'] = doc.read()
        
        # Check for examples
        if object_type in example_list['examples']:
            kwargs['examples'] = example_list['examples'][object_type]

        # Check for references
        if object_type in example_list['references']:
            references = []
            for id, reference in bib_table.iterrows():
                if reference['ID'] in example_list['references'][object_type]:
                    references.append(reference)
            kwargs['references'] = references

        # Include attributes
        attribute_list = []
        for index, row in attribute_table[attribute_table["Object_type"] == object_type].iterrows():
            attribute_item = row.to_dict()
            if os.path.isfile(f"book/doc/attributes/{object_type}-{row['Attribute_name']}.md"):
                with open(f"book/doc/attributes/{object_type}-{row['Attribute_name']}.md") as doc:
                    attribute_item['doc'] = doc.read()
            attribute_list.append(attribute_item)
        kwargs['attributes'] = attribute_list

        # Render file
        content = object_template.render(kwargs)
        filename = f"book/objects/{row['Object_type']}.md"
        with open(filename, "w") as object_file:
            object_file.write(content)
            print(f"... wrote {filename}")

command_template = env.get_template("command.md")
command_table = pd.read_csv('https://shop.sintef.energy/wp-content/uploads/sites/1/2021/11/commands_v14.csv')
command_table.columns = [c.replace(' ', '_') for c in command_table.columns]

with open(f"book/doc/commands/cross-references.yaml") as commands:
    command_list = yaml.load(commands, Loader=yaml.FullLoader)
    for index, row in command_table.iterrows():
        command_name = row["Command"]
        command_key = command_name.replace(' ', '_')
        obj = row.to_dict()
        kwargs = dict()
        kwargs['object'] = obj

        # Check for extensive doc
        if os.path.isfile(f"book/doc/commands/{command_key}.md"):
            with open(f"book/doc/commands/{command_key}.md", encoding='utf8') as doc:
                kwargs['doc'] = doc.read()
        
        # Check for examples
        if command_key in command_list['examples']:
            kwargs['examples'] = command_list['examples'][command_key]

        # Check for references
        if command_key in command_list['references']:
            references = []
            for id, reference in bib_table.iterrows():
                if reference['ID'] in example_list['references'][object_type]:
                    references.append(reference)
            kwargs['references'] = references

        # Render file
        content = command_template.render(kwargs)
        filename = f"book/commands/{command_key}.md"
        with open(filename, "w", encoding='utf8') as object_file:
            object_file.write(content)
            print(f"... wrote {filename}")

# Render TOC
toc_template = env.get_template("_toc.yml")
object_types = object_table["Object_type"].to_list()
command_types = [c.replace(' ', '_') for c in command_table["Command"].to_list()]
content = toc_template.render(
    object_types=object_types,
    command_types=command_types
)
filename = f"book/_toc.yml"
with open(filename, "w") as toc:
    toc.write(content)
    print(f"... wrote {filename}")