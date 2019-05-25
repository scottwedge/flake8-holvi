import io
import re

from setuptools import setup

with io.open('flake8_holvi.py') as f:
    version = re.search(
        r'^__version__ = [\'"]([^\'"]*)[\'"]',
        f.read(),
        re.M,
    ).group(1)

with io.open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='flake8-holvi',
    version=version,
    description='flake8 plugin to help writing Pythonic code at Holvi',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Berker Peksag',
    author_email='bpeksag@holvi.com',
    url='https://github.com/holviberker/flake8-holvi',
    py_modules=['flake8_holvi'],
    entry_points={
        'flake8.extension': [
            'HLV = flake8_holvi:HolviChecker',
        ],
    },
)