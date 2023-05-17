import io

from iterio import IterStream


def test_read() -> None:
    values = [b"abc", b"def", b"ghi"]

    result = io.BufferedReader(IterStream(values))

    assert result.read(2) == b"ab"
    assert result.read(2) == b"cd"
    assert result.read(2) == b"ef"
    assert result.read(2) == b"gh"
    assert result.read(2) == b"i"
    assert result.read(2) == b""


def test_read_text() -> None:
    values = [b"abc", b"def", b"ghi"]

    result = io.TextIOWrapper(IterStream(values))

    assert result.read(2) == "ab"
    assert result.read(2) == "cd"
    assert result.read(2) == "ef"
    assert result.read(2) == "gh"
    assert result.read(2) == "i"
    assert result.read(2) == ""
