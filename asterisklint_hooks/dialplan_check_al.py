from __future__ import annotations

import argparse
import os

from shlex import split
from typing import Sequence

from asterisklint.main import main as almain


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--alint-ignore', help='alint ignore list - comma-separated str')
    parser.add_argument('-n', '--no-odbc', action='store_true', help='do not process func_odbc.conf file')
    parser.add_argument('files', nargs='*', help='file list - one or more files')

    args = parser.parse_args(argv)

    cmd_args = 'dialplan-check '
    if args.no_odbc:
        cmd_args = cmd_args + '--func-odbc "" '
    if args.alint_ignore:
        os.environ.update(ALINT_IGNORE=args.alint_ignore)
    print(split(cmd_args))
    retval = 0
    for filename in args.files:
        cmd_args = cmd_args  + filename
        try:
            almain(split(cmd_args), os.environ)
        except Exception as exc:
            print(f'{exc}')
            retval = 1
    return retval


if __name__ == '__main__':
    raise SystemExit(main())
