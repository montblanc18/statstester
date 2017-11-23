#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

__version__ = '0.0.1'

setup(
    name = 'statstester',
    version = __version__,
    description = 'Supporting t-test & f-test.',
    long_description = '''
    statstester help you to perform t-test & f-test.
    ''',
    author = 'Shin Kurita',
    url = 'https://github.com/montblanc18',
    license = 'MIT',
    packages = find_packages(exclude = ('tests', 'docs')),
    install_requires = ['setuptools', 'scipy','numpy'],
    test_suite = 'tests'
)
