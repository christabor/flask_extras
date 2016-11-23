"""Test form wizard."""

import json

import pytest

from flask import (
    flash,
    jsonify,
    render_template,
    request,
    session,
)
from flask.ext.wtf import FlaskForm
from wtforms import (
    IntegerField,
    StringField,
    validators,
)
from flask_extras.forms.wizard import MultiStepWizard

from conftest import app


TESTING_SESSION_KEY = 'fakename'


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


@pytest.fixture(scope='module')
def ctx(request):
    with app.test_request_context() as req_ctx:
        yield req_ctx
        if TESTING_SESSION_KEY in session:
            del session[TESTING_SESSION_KEY]
        if 'MyCoolForm' in session:
            del session['MyCoolForm']


@app.route('/wizard', methods=['GET', 'POST'])
def wizard_valid_route():
    form = MyCoolForm()
    curr_step = request.args.get('curr_step')
    form_kwargs = dict(session_key=TESTING_SESSION_KEY)
    combine = 'combine' in request.args
    if curr_step is not None:
        form_kwargs.update(curr_step=curr_step)
    form = MyCoolForm(**form_kwargs)
    msg, data = None, None
    if request.method == 'POST':
        data = form.data
        if form.validate_on_submit():
            if form.is_complete():
                data = form.alldata(combine_fields=combine, flush_after=True)
                msg = 'Form validated AND COMPLETE! data = {}'.format(data)
            else:
                msg = ('Great job, but not done yet'
                       ' ({} steps remain!).'.format(form.remaining))
        else:
            msg = 'Invalid'
    return jsonify(dict(data=data, msg=msg))


@app.route('/wizard-bad', methods=['GET', 'POST'])
def wizard_invalid_route():
    form = MultiStepWizard()
    return jsonify(form.data)


def test_wizard_basic_init_nodata(client):
    app, test = client
    with pytest.raises(AssertionError):
        res = test.get('/wizard-bad')
        assert res.status_code == 500


def test_wizard_basic_init_get(client):
    app, test = client
    res = test.get('/wizard')
    assert res.status_code == 200
    data = json.loads(res.data)
    assert data['data'] is None


def test_wizard_basic_init_post(client):
    app, test = client
    res = test.post('/wizard', data=dict(field1='Foo', field2=2))
    assert res.status_code == 200
    data = json.loads(res.data)
    assert data['data'] == dict(field1='Foo', field2=2)


def test_wizard_basic_post_jumpstep(client):
    app, test = client
    res = test.post('/wizard?curr_step=2',
                    data=dict(field3='Foo', field4=4))
    assert res.status_code == 200
    data = json.loads(res.data)
    assert data['data'] == dict(field3='Foo', field4=4)


def test_wizard_post_fullsteps(ctx, client):
    app, test = client
    res1 = test.post('/wizard?curr_step=1',
                     data=dict(field1='Foo', field2=2))
    res2 = test.post('/wizard?curr_step=2',
                     data=dict(field3='Foo', field4=4))
    assert res1.status_code == 200
    assert res2.status_code == 200
    data = json.loads(res2.data)
    assert data['data'] == dict(field3='Foo', field4=4)


def test_wizard_post_bad_fieldtype(ctx, client):
    app, test = client
    res1 = test.post('/wizard?curr_step=1',
                     data=dict(field1=1, field2=2))
    res2 = test.post('/wizard?curr_step=2',
                     data=dict(field3='Foo', field4='Foo'))
    assert res1.status_code == 200
    assert res2.status_code == 200
    data = json.loads(res2.data)
    assert data['data']['field4'] is None
    assert data['msg'] == 'Invalid'


def test_form_is_complete(client):
    form = MyCoolForm()
    assert not form.is_complete()


def test_form_setfields(client):
    form = MyCoolForm()
    assert len(form._unbound_fields) == 1
    assert len(form.__forms__) == 2
    # Confirm it's obfuscated for non-local access.
    assert not hasattr(form, '__forms')


def test_form_get_data(client):
    app, test = client
    form = MyCoolForm()
    assert form.data == dict(field1=None, field2=None)


def test_form_get_alldata(client):
    form = MyCoolForm()
    assert form.alldata() == dict(
        MultiStepTest1=None,
        MultiStepTest2=None,
    )


def test_form_get_alldata_combined_none(client):
    form = MyCoolForm()
    assert form.alldata(combine_fields=True) == dict()


def test_form_populate_forms(client):
    form = MyCoolForm()
    assert len(form.forms) == 2


def test_form_populate_forms_once_only(client):
    form = MyCoolForm()
    form._populate_forms()
    form._populate_forms()
    assert len(form.forms) == 2


def test_form_active(client):
    form = MyCoolForm()
    assert form.active_name == 'MultiStepTest1'
    assert isinstance(form.active_form, MultiStepTest1)


def test_form_step_attrs(client):
    form = MyCoolForm()
    assert form.step == 1
    assert form.total_steps == 2
    assert form.remaining == 2
    assert form.steps == [1, 2]


def test_form_flush(client):
    form = MyCoolForm()
    assert 'MyCoolForm' in session
    form.flush()
    assert 'MyCoolForm' not in session


def test_form_validate_on_submit(client):
    form = MyCoolForm()
    assert not form.validate_on_submit()


def test_form_len_override(client):
    form = MyCoolForm()
    assert len(form) == 2
