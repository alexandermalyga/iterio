import io
from collections.abc import Iterable
from typing import Any


class IterStream(io.RawIOBase):
    """
    Serves an iterable of bytes as a read-only file-like binary stream. Reading
    should be done by wrapping an instance of this class with an
    io.BufferedReader or io.TextIOWrapper object.
    """

    def __init__(self, iterable: Iterable[bytes]) -> None:
        self._iter = iter(iterable)
        self._leftover = None

    def readinto(self, buffer: Any) -> int:
        try:
            chunk = self._leftover or next(self._iter)
        except StopIteration:
            return 0

        size = len(buffer)
        output, self.leftover = chunk[:size], chunk[size:]
        buffer[: len(output)] = output
        return len(output)

    def readable(self) -> bool:
        return True
