from setuptools import setup, find_packages

setup(
    name='smartformatter',
    version='0.1',
    packages=find_packages(),
    install_requires=['inflect'],
    author='shankar',
    description='utility function for smart formatting of names, phones, numbers.'
)
