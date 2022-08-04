import yaml
import pandas as pd
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("templates/"))

object_template = env.get_template("object.md")
object_table = pd.read_csv('https://shop.sintef.energy/wp-content/uploads/sites/1/2022/04/objects_v14.csv')
object_table.columns = [c.replace(' ', '_') for c in object_table.columns]

with open(f"book/objects/examples.yaml") as examples:
    example_list = yaml.load(examples, Loader=yaml.FullLoader)
    for index, row in object_table.iterrows():
        obj = row.to_dict()
        if isinstance(row["Legal_output_connections"], str):
            obj['Legal_output_connections'] = [o.strip() for o in obj['Legal_output_connections'].split(',')]
        else:
            obj['Legal_output_connections'] = []
        kwargs = dict()
        kwargs['object'] = obj
        
        # Check for extensive doc
        object_type = row["Object_type"]
        if object_type in example_list['doc']:
            with open(f"book/{example_list['doc'][object_type]}.md") as doc:
                kwargs['doc'] = doc.read()
        
        # Check for examples
        if object_type in example_list['examples']:
            kwargs['examples'] = example_list['examples'][object_type]

        # Render file
        content = object_template.render(kwargs)
        filename = f"book/objects/{row['Object_type']}.md"
        with open(filename, "w") as object_file:
            object_file.write(content)
            print(f"... wrote {filename}")
