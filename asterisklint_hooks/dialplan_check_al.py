from __future__ import annotations

import argparse
import os
from shlex import split
from typing import Sequence

from asterisklint.main import main as almain  # type: ignore


def main(argv: Sequence[str] | None = None) -> int:  # pylint: disable=duplicate-code
    parser = argparse.ArgumentParser(
        description='Run asterisklint.main on configuration files'
    )
    parser.add_argument(
        '-a', '--alint-ignore', nargs=1, help='alint ignore list - comma-separated str'
    )
    parser.add_argument(
        '-n', '--no-odbc', action='store_true', help='do not process func_odbc.conf file'
    )
    parser.add_argument('files', nargs='*', help='file list - one or more files')

    args = parser.parse_args(argv)

    cmd_args = 'dialplan-check '
    if args.no_odbc:
        cmd_args = cmd_args + '--func-odbc "" '
    if args.alint_ignore:
        os.environ.update(ALINT_IGNORE=args.alint_ignore)

    retval = 0
    for filename in args.files:
        cmd_args = cmd_args + filename
        try:
            retval = almain(split(cmd_args), os.environ)
        except (IOError, RuntimeError) as exc:
            print(f'{exc}')
            retval = 2
    return retval


if __name__ == '__main__':
    raise SystemExit(main())
