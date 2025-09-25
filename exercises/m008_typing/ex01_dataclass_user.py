"""
Bài tập: Dataclass & typing (mức vừa-khá)
- Tạo dataclass User(id: int, name: str, email: str)
- Thêm method is_valid_email() -> bool
- Viết hàm users_to_index(users) -> dict[int, User]
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class User:
    # TODO: định nghĩa field
    ...

    def is_valid_email(self) -> bool:
        # TODO: check ký tự '@'
        raise NotImplementedError


def users_to_index(users: List[User]) -> Dict[int, User]:
    raise NotImplementedError
