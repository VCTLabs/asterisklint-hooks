from __future__ import annotations

import argparse
import subprocess as sp

from os import environ
from shlex import split
from typing import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--alint-ignore', help='alint ignore list - comma-separated str')
    parser.add_argument('-n', '--no-odbc', action='store_true', help='do not process func_odbc.conf file')
    parser.add_argument('files', nargs='*', help='file list - one or more files')

    args = parser.parse_args(argv)

    cmd_args = 'asterisklint dialplan-check '
    if args.no_odbc:
        cmd_args = cmd_args + '--func-odbc "" '

    if args.alint_ignore:
        environ.update(ALINT_IGNORE=args.alint_ignore)

    retval = 0
    for filename in args.files:
        cmd_args = cmd_args  + filename
        cmd = split(cmd_args)
        try:
            sp.run(cmd, env=environ)
        except Exception as exc:
            print(f'{exc}')
            retval = 1
    return retval


if __name__ == '__main__':
    raise SystemExit(main())
