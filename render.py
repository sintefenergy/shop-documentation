import os
import yaml
import pandas as pd
from jinja2 import Environment, FileSystemLoader
import bibtexparser

env = Environment(loader=FileSystemLoader("templates/"))

object_table = pd.read_csv('https://shop.sintef.energy/wp-content/uploads/sites/1/2022/04/objects_v14.csv')
object_table.columns = [c.replace(' ', '_') for c in object_table.columns]

object_template = env.get_template("object.md")
with open(f"book/objects/cross-references.yaml") as examples:
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
        if os.path.isfile(f"book/doc/{object_type}.md"):
            with open(f"book/objects/{object_type}.md") as doc:
                kwargs['doc'] = doc.read()
        
        # Check for examples
        if object_type in example_list['examples']:
            kwargs['examples'] = example_list['examples'][object_type]

        # Check for examples
        if object_type in example_list['references']:
            with open('book/references.bib') as bibfile:
              bib_list = bibtexparser.load(bibfile)
            table = pd.DataFrame(bib_list.entries)
            ## Available entries
            # ['year', 'url', 'volume', 'title', 'pages', 'keywords', 'journal',
            #      'isbn', 'doi', 'author', 'ENTRYTYPE', 'ID', 'abstract', 'publisher',
            #      'month', 'issn', 'issue'],
            table = table[['ID', 'author', 'title', 'journal', 'year', 'url', 'doi', 'abstract']].reset_index()
            references = []
            for id, reference in table.iterrows():
                if reference['ID'] in example_list['references'][object_type]:
                    references.append(reference)
            kwargs['references'] = references

        # Render file
        content = object_template.render(kwargs)
        filename = f"book/objects/{row['Object_type']}.md"
        with open(filename, "w") as object_file:
            object_file.write(content)
            print(f"... wrote {filename}")

toc_template = env.get_template("_toc.yml")
object_types = object_table["Object_type"].to_list()
content = toc_template.render(object_types=object_types)
filename = f"book/_toc.yml"
with open(filename, "w") as toc:
    toc.write(content)
    print(f"... wrote {filename}")