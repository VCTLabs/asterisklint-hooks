import sys

import pytest

from asterisklint_hooks.dialplan_check_al import main


@pytest.mark.parametrize("option", ("-h", "--help"))
def test_help(capsys, option):
    try:
        main([option])
    except SystemExit:
        pass
    output = capsys.readouterr().out
    assert "Run asterisklint.main on" in output


@pytest.mark.parametrize("odbc", (None, "-n", "--no-odbc"))
def test_with_odbc(capfd, odbc):
    args = []
    if odbc:
        args += [odbc]
    main(args)


@pytest.mark.parametrize("ignore", ("-a", "--alint-ignore"))
def test_with_ignore_missing(capsys, ignore):
    args = []
    if ignore:
        args += [ignore]
    with pytest.raises(SystemExit):
        main(args)
        output = capsys.readouterr().out
        assert "expected 1 argument" in output


def test_bogus_data(monkeypatch, capfd, tmpdir):
    extensions = str(tmpdir / "extensions.conf")
    open(extensions, "w").write("one\ntwo\nthree\n")
    with monkeypatch.context() as m:
        m.setattr(sys, 'argv', [extensions])
        main(sys.argv)
        out = capfd.readouterr().err
        assert 'E_CONF_BAD_LINE' in out


def test_good_data(monkeypatch, capfd, tmpdir):
    extensions = str(tmpdir / "extensions.conf")
    open(extensions, "w").write("[general]\nstatic=yes\n\n[globals]\n")
    with monkeypatch.context() as m:
        m.setattr(sys, 'argv', [extensions])
        main(sys.argv)
        out = capfd.readouterr().err
        assert '' in out
