{# This is a comment #}

{# First we need to say which template we're extending.
   full.tpl is the default template for HTML output. #}
{%- extends 'full.tpl' -%}

{# Now to override some blocks. #}

{%- block markdowncell -%}
<div style="background-color: hsl(85, 86%, 76%);">
{# super() means 'put here whatever the parent template does for this block' #}
{{ super() }}
</div>
{%- endblock markdowncell -%}
