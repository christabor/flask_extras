[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1f8f45e92a9b4ed1ab5029ee7a0e5534)](https://www.codacy.com/app/dxdstudio/flask_extras?utm_source=github.com&utm_medium=referral&utm_content=christabor/flask_extras&utm_campaign=badger)
[![Build Status](https://travis-ci.org/christabor/flask_extras.svg?branch=master)](https://travis-ci.org/christabor/flask_extras)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/christabor/flask_extras/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/christabor/flask_extras/?branch=master)
[![Code Climate](https://codeclimate.com/github/christabor/flask_extras/badges/gpa.svg)](https://codeclimate.com/github/christabor/flask_extras)
[![Coverage Status](https://coveralls.io/repos/github/christabor/flask_extras/badge.svg?branch=master)](https://coveralls.io/github/christabor/flask_extras?branch=master)
[![Code Health](https://landscape.io/github/christabor/flask_extras/master/landscape.svg?style=flat)](https://landscape.io/github/christabor/flask_extras/master)

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

## Available features

### Views

Import them like usual:

```python
from flask_extras.views import (
    statuses,
)
```

*Note:* each view must have a valid template in your apps templates dir. See each view for the required names and locations.

*Note:* each view has configuration helpers to inject or configure your app. See source for details.

### Macros

**Many more macros** are available. You can use them like so:

```html
{% from 'macros.html' import list_group, objects2table %}
```

For the most comprehensive docs, check out each [macro](flask_extras/macros/). Comment "docstrings" are inline using jinja2 comments (these are not rendered in your html).

Also, check the source and/or output to see what classes are available for style overrides.

### Statuses

Provides views for common status codes. Usage:

```python
app = statuses.inject_error_views(app)
```

See source for more.

### Decorators

See the source for more. Usage example:

```python
from flask_extras.decorators import require_headers

app.route('/')
@require_headers(['X-Foo'])
def foo():
    pass
```


### Forms

#### WTForm Multi-step wizard

A WTForm extension for handling an arbitrary number of separate forms as a single, multi-step, multi-POST wizard. All state and data are handled by apps' session backend. Building forms is just like you're used to -- simple and intuitive. Just inherit the `MultiStepWizard` class and put a `__forms__` key on it, which is just a list of all the forms you want to use. *Note*: list order matters for your form steps.

Usage example:

```python
from flask.ext.wtf import FlaskForm

from flask_extras.forms.wizard import MultiStepWizard


class MultiStepTest1(FlaskForm):
    field1 = StringField(validators=[validators.DataRequired()],)
    field2 = IntegerField(validators=[validators.DataRequired()],)


class MultiStepTest2(FlaskForm):
    field3 = StringField(validators=[validators.DataRequired()],)
    field4 = IntegerField(validators=[validators.DataRequired()],)


class MyCoolForm(MultiStepWizard):
    __forms__ = [
        MultiStepTest1,
        MultiStepTest2,
    ]
```

and an example route:

```python
from forms import MyCoolForm

@app.route('/', methods=['GET', 'POST'])
def index():
    curr_step = request.args.get('curr_step')
    form_kwargs = dict(session_key='mycustomkey')
    if curr_step is not None:
        form_kwargs.update(curr_step=curr_step)
    form = forms.MyCoolForm(**form_kwargs)
    kwargs = dict(form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.is_complete():
                data = form.alldata(combine_fields=True, flush_after=True)
                flash('Form validated and complete! data = {}'.format(data),
                      'success')
                return jsonify(data)
            else:
                flash('Great job, but not done yet ({} steps remain!).'.format(form.remaining))
        else:
            flash('Invalid form data.', 'error')
    return render_template('index.html', **kwargs)
```

and an example html page (using the [wtform_form](flask_extras/macros/macros.html) macro also available):

```html
{% if form.is_complete() %}
    <span class="well">Complete!</span>
{% else %}
    <ul class="list-inline">
        {% for step in form.steps %}
            <li>
                {% if step == form.curr_step %}
                    <strong class="lead label label-info">current {{ step }}</strong>
                {% else %}
                    <a href="{{ url_for('app.index') }}?curr_step={{ step }}">{{ step }}</a>
                {% endif %}
                {% if not loop.last %}
                    &nbsp;&nbsp;/
                {% endif %}
            </li>
        {% endfor %}
    </ul>
    {{ wtform_form(form,
        classes=['form', 'form-horizontal'],
        btn_classes=['btn btn-primary', 'btn-lg'],
        align='right',
        action=url_for('app.index'),
        method='POST',
        reset_btn=False,
        horizontal=True,
    ) }}
{% endif %}
```
