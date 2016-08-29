# Macros

An assortment of macros have been created for various reusable templating scenarios.

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

### bs3_dictlist_group

...

### bs3_list_group

...

### dictlist2nav

...

### dictlist2dropdown

...

### dictlist2checkboxes

...

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

## `code.html`

...

## `messages.html`

...
