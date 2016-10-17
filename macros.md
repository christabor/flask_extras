# Macros

An assortment of macros have been created for various reusable templating scenarios.

*New in 3.6.1* - namedtuple support on all dictionary based macros.

E.g.

```python
from collections import namedtuple
Person = namedtuple('Person', 'age dob sex loc name')
person=Person(30, '01051986', 'M', 'seattle', 'chris')
```

Can now be used with any macro that supports `asdict` kwarg:

`{{ dict2list(person, asdict=True) }}`

## `macros.html`

### apply_classes

Apply a list of classes inline.

```jinja2
<table class="{{ apply_classes(['table', 'table-striped']) }}"></table>
```

becomes:

```html
<table class="table table-striped"></table>
```

### apply_dattrs

Apply a list of HTML5 data-attributes inline.

```jinja2
<table class="{{ apply_dattrs(['datatable', 'sortable']) }}"></table>
```

becomes:

```html
<table data-datatable data-sortable></table>
```

### dictlist_dl

...

### dict2list

...

### dictlist2nav

...

### dictlist2dropdown

Convert a dict into a dropdown of options.

```jinja2
{{
  dictlist2dropdown({'foo': 'bar', 'bar': 'foo'}, 'options', classes=['form-dropdown'])
}}
```

becomes

```html
<select name="options" class="form-dropdown">
  <option value="foo">bar</option>
  <option value="bar">foo</option>
</select>
```

### dictlist2checkboxes

Convert a dictionary into a fieldset of checkboxes.

```jinja2
{{
  dictlist2checkboxes({'foo': 'bar', 'bar': 'foo'}, fieldset_class='someclass')
}}
```

becomes

```html
<fieldset>
  <label>
    foo <input type="checkbox" name="bar">
  </label>
  <label>
    bar <input type="checkbox" name="foo">
  </label>
</fieldset>
```

### objects2table

Create a table with headers and rows for a list of objects. Major customization is possible, even on a per column basis, by using the `field_macros` kwarg.

```jinja2
{{
    objects2table([obj1, obj2, obj3]
                  classes=['table', 'table-striped'],
                  data_attrs=['datatable'],
                  filterkeys=['some_secret_key1', 'some_secret_key2'],
                  filtervals=['someval1', 'secret name'],
                  pk_link='/some/link/',
                  field_macros={
                        'field1': mymacro1,
                        'field2': mymacro2,
                    },
                  )
}}
```

### wtform_errors

Show a list of form errors based on a given wtform instance.

### wtform_form

Automatically render a wtform object, with various options including horizontal/vertical layouts, alignment, field overrides and more.

```jinja2
{{
  wtform_form(form,
    action=url_for('app.index'),
    method='POST',
    classes=['form', 'form-horizontal'],
    btn_classes=['btn', 'btn-primary', 'btn-md'],
    align='right',
    horizontal=True,
  )
}}
```

And using field specific overrides:

```jinja2
{%- macro somefieldmacro(field) %}
Look at my great field! {{ field.label }} {{ field }}
{% endmacro -%}

{{
  wtform_form(form,
    field_macros={
      'somefield': somefieldmacro
    }
  )
}}
```

The field object passed to your macro is a standard wtform field object.

### recurse_dictlist

Uses the jinja2 recursive looping to recurse over a dictionary and display as a list (ordered or unordered), or display a default value otherwise.

### dict2labels

...

### list2list

...

## `code.html`

### code

```jinja2
{{ code('a, b, c = 1, 2, 3', lang='python') }}
```

becomes

```html
<pre class="python">
  <code>a, b, c = 1, 2, 3</code>
</pre>
```

### inline_code

```jinja2
{{ inline_code('a, b, c = 1, 2, 3') }}
```

becomes

```html
<code>a, b, c = 1, 2, 3</code>
```

## `messages.html`

### flash_messages

Render a flask messages object inline, including background coloring (using bootstrap) for each status type (e.g. info, warning, error)

```jinja2
{{  flash_messages() }}
```

## `content_blocks.html`

### dict_heading_blocks
