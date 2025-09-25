"""
Bài tập: Delegation & composition (mức nâng cao)
- Class Book(title, author)
- Class Library quản lý nhiều Book: add_book, find_by_title, remove_title
- Lưu ý: không trả về tham chiếu trực tiếp đến list nội bộ
"""
from typing import List, Optional


class Book:
    def __init__(self, title: str, author: str) -> None:
        # TODO: validate
        raise NotImplementedError


class Library:
    def __init__(self) -> None:
        # TODO
        raise NotImplementedError

    def add_book(self, book: Book) -> None:
        raise NotImplementedError

    def find_by_title(self, title: str) -> Optional[Book]:
        raise NotImplementedError

    def remove_title(self, title: str) -> bool:
        """Xóa sách theo title, trả về True nếu xóa được."""
        raise NotImplementedError
