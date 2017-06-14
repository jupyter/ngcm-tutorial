# Custom templates for nbconvert

This directory contains three nbconvert templates to hide code cells:

- `hidecode.tplx` : Latex, hide all code cells
- `hidecode_selective.tplx` : Latex, hide only code cells indicated by metadata
- `foldcode.tpl` : HTML, hide code cells indicated by metadata, and add buttons to
  show and hide each code cell individually.

For the latter two, you can mark code cells that should be hidden by adding this
JSON to their metadata (select the 'Edit Metadata' cell toolbar):

```javascript
"nbconvert": {
  "hide_code": true
}
```

To use the templates at the command line:

```shell
ipython nbconvert --to latex --template hidecode.tplx MyNotebook.ipynb

ipython nbconvert --to latex --template hidecode_selective.tplx MyNotebook.ipynb

ipython nbconvert --to html --template foldcode.tpl MyNotebook.ipynb
```
