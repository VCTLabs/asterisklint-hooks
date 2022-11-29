from __future__ import annotations

from setuptools import setup


with open(".version", 'r') as f:
    AL_VERSION = f.read().strip()


setup(
    install_requires=[f'asterisklint=={AL_VERSION}'],
)
