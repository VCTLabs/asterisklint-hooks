from __future__ import annotations

from pathlib import Path

from setuptools import setup

AL_VERSION = Path(__file__).with_name("version.txt").read_text().strip()


if __name__ == "__main__":
    setup(
        name="asterisklint_hooks",
        version="{}".format(AL_VERSION),
        install_requires=["asterisklint=={}".format(AL_VERSION)],
    )
