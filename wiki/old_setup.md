## Older setup

~~Since the nature of macros and filters makes it harder to import as a standard package, the best way to use this project is as a git submodule. This can be done easily, just use `git submodule add https://github.com/christabor/flask_extras.git` inside your current git project. This allows easy updates.~~

This project has been converted a proper python package. You can use it easily in the same way as before, but without the headache of submodules.

## Testing

Run `nosetests .`

## Registering filters
It's easy. All filters are registered at once, using the following command:

```python
from flask_extras.filters import config as filter_conf

filter_conf.config_flask_filters(app)
```

## Using macros

The best way is to add the templates to your jinja instance, rather than having to move folders around after cloning the module.

This can be done using the following

### As a submodule:

```python
import os
import jinja2

extra_folders = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader('{}/flask_extras/macros/'.format(os.getcwd())),
])
app.jinja_loader = extra_folders
```

### As a package:

```python
import os
import jinja2

from flask_extras import macros as extra_macros

extra_folders = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader(os.path.dirname(extra_macros.__file__)),
])
app.jinja_loader = extra_folders
```

Which will load the default `templates` folder, and the new macros.

Now, just import them like any other macro!
