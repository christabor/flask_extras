[![Build Status](https://travis-ci.org/christabor/flask_extras.svg?branch=master)](https://travis-ci.org/christabor/flask_extras)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/christabor/flask_extras/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/christabor/flask_extras/?branch=master)
[![Code Climate](https://codeclimate.com/github/christabor/flask_extras/badges/gpa.svg)](https://codeclimate.com/github/christabor/flask_extras)

# Flask Extras
Assorted useful flask views, blueprints, Jinja2 template filters, and templates/macros.

## Overall setup

As of `3.4.0`, filters and templates will automatically be registered and available through the following simple command:

```python
from flask_extras import FlaskExtras
app = Flask('myapp')
FlaskExtras(app)
```

For the old way, check out [this page](wiki/old_setup.md)

```html
{% from 'macros.html' import list_group, objects2table %}
```

See [macros](macros.md) page for details.

## Using views

Import them like usual:

```python
from flask_extras.views import (
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
