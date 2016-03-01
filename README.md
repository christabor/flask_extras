# jinja2-filters
Filters for jinja2 templating language.

## Overall setup

Since the nature of macros and filters makes it harder to import as a standard package, the best way to use this project is as a git submodule. This can be done easily, just use `git submodule add https://github.com/christabor/jinja2-template-pack` inside your current git project. This allows easy updates.

## Registering filters
It's easy. All filters are registered at once, using the following command:

```python
from jinja2_template_pack.filters import config as filter_conf

filter_conf.config_flask_filters(app)
```

## Using macros

The best way is to add the templates to your jinja instance, rather than having to move folders around after cloning the module.

This can be done using the following:

```python
import os
import jinja2

extra_folders = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader('{}/jinja2_template_pack/macros/'.format(os.getcwd())),
])
app.jinja_loader = extra_folders
```

Which will load the default `templates` folder, and the new macros.

Now, just import them like any other macro:

```html
{% from 'macros.html' import list_group, objects2table %}
```

## Using views

Import them like usual:

```python
from jinja2_template_pack.views import (
    statuses,
)
```

*Note:* each view must have a valid template in your apps templates dir. See each view for the required names and locations.

*Note:* each view has configuration helpers to inject or configure your app. See source for details.

#### Statuses

Provides views for common status codes. Usage:
```python
app = statuses.inject_error_views(app)
```

