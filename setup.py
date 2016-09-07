"""Setup for Flask Extras."""

from setuptools import find_packages, setup

SRCDIR = '.'
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
    version='3.6.1',
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
