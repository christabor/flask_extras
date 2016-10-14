"""Setup for Flask Extras."""

from setuptools import setup

requirements = [
    'Flask==0.10.1',
]


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
            return __doc__


setup(
    name='flask_extras',
    version='3.6.2',
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
    install_requires=requirements,
    package_dir={'flask_extras': 'flask_extras'},
    packages=['flask_extras'],
    package_data={
        'flask_extras': [
            'macros/*.html',
        ],
    },
    zip_safe=False,
    include_package_data=True,
)
