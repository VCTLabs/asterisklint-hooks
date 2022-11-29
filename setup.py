from __future__ import annotations

from pathlib import Path

from setuptools import setup
from versioningit import get_cmdclasses

AL_VERSION = Path(__file__).with_name(".version").read_text().strip()


setup(
    cmdclass=get_cmdclasses(),
    name="asterisklint_hooks",
    version="{}".format(AL_VERSION),
    install_requires=["asterisklint=={}".format(AL_VERSION)],
)
