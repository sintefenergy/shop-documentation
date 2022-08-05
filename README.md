# SHOP documentation
The SHOP documentation is built using [Jupyter Book](https://jupyterbook.org/en/stable/intro.html). The command, object and attribute documentation is auto-generated based on the short-descriptions in the SHOP source code. The object description is rendered using [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) with the template(s) in [](/templates/) by running the script [](/render.py). The whole process is automated with the workflow [](/.github/workflows/jupyter-books.yaml).

For local development and testing, execute the following commands to generate the book:
```
python render.py
jupyter book build .\book\
```
To inspect the book, open `/book/_build/html/intro.html`

## Update documentation
To include additional description, examples and references, please follow this guideline.

## Additional command description
Additional command description can be added by adding markdown files in the [/book/doc/commands/](/book/doc/commands/) folder. The file name should be the same as the command type, but white space should be replaced with underscore (_). The file should not containt level one headings (#). The content of the file will be automatically merged into the object type documentation by Github Actions.

### Additional object description
Additional object description can be added by adding markdown files in the [](/book/doc/objects/) folder. The file name should be the same as the object type and should not containt level one headings (#). The content of the file will be automatically merged into the object type documentation by Github Actions.

### Additional attribute description
Additional attribute description can be added by putting markdown files in the [](/book/doc/attributes/) folder. The file name should be `{object_type}-{attribute_name}.md` and should note contain level one (#) or two (##) headings. The content of the file will be automatically merged into the object type documentation and can be hyperlinked to with `[]({object_type}:{attribute_name}})` anywhere in the documentation.

### Examples
Examples can be added in the [](/book/examples/) folder. Use sub-folders if necessary to keep the structure clean. The examples should be listed in the [table of contents](/templates/_toc.yml) as a chapter in *Examples and tutorials*. The examples should also be listed under the relevant objects in [](book/objects/cross-references.yaml).

### References
References to scientific publications should be included in [](book/references.bib). Make sure the entry is not a duplicate of existing entries. Add reference to the new publication for the relevant objects in [](book/objects/cross-references.yaml) such that they appear it the automatically generated object documentation.
