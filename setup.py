"""Setup for Flask Extras."""

from setuptools import setup, find_packages
import os

SRCDIR = '.'


def readme():
    """Grab the long README file."""
    try:
        with open('README.md', 'r') as fobj:
            return fobj.read()
    except IOError:
        try:
            with open('README.rst', 'r') as fobj:
                return fobj.read()
        except IOError:
            return 'No README specified.'


def get_requires():
    """Extract the requirements from a standard requirements.txt file."""
    path = '{}/requirements.txt'.format(
        os.path.abspath(os.path.dirname(__file__)))
    with open(path) as reqs:
        return [req for req in reqs.readlines() if req]

setup(
    name='flask_extras',
    version='3.4.0',
    description=('Assorted useful flask views, blueprints, '
                 'Jinja2 template filters, and templates/macros'),
    long_description=readme(),
    author='Chris Tabor',
    author_email='dxdstudio@gmail.com',
    url='https://github.com/christabor/flask_extras',
    license='MIT',
    classifiers=[
        'Topic :: Software Development',
        'Programming Language :: Python :: 2.7',
    ],
    package_dir={'': SRCDIR},
    packages=find_packages(SRCDIR, exclude=['ez_setup', 'examples', 'tests']),
    package_data={
        'flask_extras': [
            'macros/*.html',
        ],
    },
    zip_safe=False,
    include_package_data=True,
)
