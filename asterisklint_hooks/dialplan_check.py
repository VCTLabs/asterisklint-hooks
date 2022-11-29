from __future__ import annotations

import argparse
import logging
import subprocess as sp  # nosec (yes we need this)
from os import environ
from shlex import split
from typing import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-a', '--alint-ignore', help='alint ignore list - comma-separated str'
    )
    parser.add_argument(
        '-n', '--no-odbc', action='store_true', help='do not process func_odbc.conf file'
    )
    parser.add_argument('files', nargs='*', help='file list - one or more files')

    args = parser.parse_args(argv)

    cmd_args = 'asterisklint dialplan-check '
    if args.no_odbc:
        cmd_args = cmd_args + '--func-odbc "" '

    if args.alint_ignore:
        environ.update(ALINT_IGNORE=args.alint_ignore)

    retval = 0
    for filename in args.files:
        cmd_args = cmd_args + filename
        cmd = split(cmd_args)
        try:
            # rus in pre-commit env, otherwise sanitized
            sp.run(cmd, shell=False, check=True, env=environ, timeout=5)  # nosec
        except (sp.CalledProcessError, sp.TimeoutExpired) as exc:
            logging.debug('%s', exc)
            retval = 1
    return retval


if __name__ == '__main__':
    raise SystemExit(main())
