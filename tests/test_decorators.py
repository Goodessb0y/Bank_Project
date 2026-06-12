import pytest

from decorators import log


def test_log_success_to_console(capsys):
    @log()
    def add(x, y):
        return x + y

    result = add(1, 2)

    captured = capsys.readouterr().out.strip()

    assert result == 3
    assert captured == "add ok"


def test_log_success_to_file(tmp_path):
    file = tmp_path / "log.txt"

    @log(filename=str(file))
    def mul(x, y):
        return x * y

    mul(2, 3)

    content = file.read_text().strip()

    assert content == "mul ok"


def test_log_error_to_console(capsys):
    @log()
    def fail(x):
        raise ValueError("bad input")

    with pytest.raises(ValueError):
        fail(10)

    captured = capsys.readouterr().out.strip()

    assert "fail error: ValueError" in captured
    assert "Inputs: (10,)" in captured


def test_log_error_to_file(tmp_path):
    file = tmp_path / "log.txt"

    @log(filename=str(file))
    def fail(x):
        raise RuntimeError("boom")

    with pytest.raises(RuntimeError):
        fail(1)

    content = file.read_text().strip()

    assert "fail error: RuntimeError" in content
    assert "Inputs: (1,)" in content