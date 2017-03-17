"""A Test app to demonstrate various aspects of flask_extras."""

from collections import OrderedDict
from datetime import datetime as dt

from flask import (
    Flask,
    render_template,
    flash,
    request,
)

from flask_wtf import FlaskForm

from flask_extras import FlaskExtras
from wtforms import (
    BooleanField,
    IntegerField,
    RadioField,
    HiddenField,
    PasswordField,
    SelectField,
    SelectMultipleField,
    StringField,
    SubmitField,
    TextAreaField,
    validators,
)

from flask_extras.views import statuses

app = Flask('flask_extras_test')
app.secret_key = 'abc1234'

FlaskExtras(app)


class SomeForm(FlaskForm):
    """Form."""

    hideme = HiddenField()
    favorite_food = RadioField(
        choices=[('pizza', 'Pizza'), ('ice-cream', 'Ice Cream')]
    )
    age = IntegerField(validators=[validators.DataRequired()])
    name = StringField(
        description='enter your name',
        validators=[validators.DataRequired()],
    )
    nickname = StringField('What do people call you?')


class SomeForm2(FlaskForm):
    """Form."""

    hideme = HiddenField()
    frobnicate = BooleanField()
    baz = StringField()
    quux = SelectMultipleField(
        choices=[(v, v) for v in ['quux', 'baz', 'foo']])


@app.context_processor
def ctx():
    """Add global ctx."""
    return dict(
        ghub_url='https://github.com/christabor/flask_extras/blob/master/flask_extras/macros/',
        name=str(request.url_rule),
        links=sorted(get_rulesmap()),
    )


def get_rulesmap():
    """Get all rules so we ensure they're dynamic and always updated."""
    bad = ['static', 'index']
    return [r.endpoint for r in app.url_map._rules if r.endpoint not in bad]


@app.route('/')
def index():
    """Demo page links."""
    return render_template('pages/index.html', **dict(home=True))


@app.route('/extras_msg.html')
def extras_msg():
    """Demo page."""
    flash('I am a success message!', 'success')
    flash('I am warning message!', 'warning')
    flash('I am an error (danger) message!', 'error')
    flash('I am an info message!', 'info')
    return render_template('pages/extras_msg.html')


@app.route('/content_blocks.html')
def content_blocks():
    """Demo page."""
    return render_template('pages/content_blocks.html')


@app.route('/extras_code.html')
def extras_code():
    """Demo page."""
    return render_template('pages/extras_code.html')


@app.route('/dates.html')
def dates():
    """Demo page."""
    kwargs = dict(somedate=dt.now())
    return render_template('pages/dates.html', **kwargs)


@app.route('/utils.html')
def utils():
    """Demo page."""
    kwargs = dict()
    return render_template('pages/utils.html', **kwargs)


@app.route('/macros.html')
def macros():
    """Demo page."""
    kwargs = dict(
        dicttest=dict(
            foo='Some bar',
            bar='Some foo',
        ),
        dictlist=[
            dict(
                foo='Some bar',
                bar='Some foo',
            )
        ],
        dictlist2=[
            dict(name='foo', age=10, dob='01/01/1900', gender='M'),
            dict(name='bar', age=22, dob='01/01/1901', gender='F'),
            dict(name='quux', age=120, dob='01/01/1830', gender='X'),
        ],
        form=SomeForm(),
        recursedict=vars(request),
    )
    return render_template('pages/macros.html', **kwargs)


@app.route('/bootstrap.html')
def bootstrap():
    """Demo page."""
    dicttest = dict(
        foo='Some bar',
        bar='Some foo',
    )
    dictlist = [
        dict(name='zomb', age=999, dob='03/01/2030', gender='Z102'),
        dict(name='foo', age=10, dob='01/01/1900', gender='M'),
        dict(name='bar', age=22, dob='01/01/1901', gender='F'),
        dict(name='quux', age=120, dob='01/01/1830', gender='X'),
    ]
    kwargs = dict(
        dicttest=dicttest,
        dictlist=dictlist,
        form=SomeForm(),
        form2=SomeForm2(),
        pagination=OrderedDict(
            zip(['/somelink/{}'.format(i) for i in range(10)], range(10))
        ),
    )
    return render_template('pages/bootstrap.html', **kwargs)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5014)
