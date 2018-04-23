from os import path
from setuptools import setup, find_packages
from codecs import open

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='hello', 
    version='0.1.0',
    description='say hello',
    long_description=long_description,
    packages=find_packages(),
    entry_points={
        'console_scripts':['hello=hello:main']
    })