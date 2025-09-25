"""
Bài tập: Protocols (mức nâng cao)
- Tạo Protocol Sortable với method key() -> tuple
- Viết class Song(title, plays) implement giao diện Sortable
- Hàm sort_by_key(items: list[Sortable]) -> list[Sortable]
"""
from __future__ import annotations
from typing import Protocol, Tuple, List


class Sortable(Protocol):
    def key(self) -> Tuple:
        ...  # pragma: no cover


class Song:
    def __init__(self, title: str, plays: int) -> None:
        # TODO
        raise NotImplementedError

    def key(self) -> Tuple:
        # TODO: (plays DESC, title ASC)
        raise NotImplementedError


def sort_by_key(items: List[Sortable]) -> List[Sortable]:
    raise NotImplementedError
