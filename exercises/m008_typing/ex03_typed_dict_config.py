"""
Bài tập: TypedDict & validation (mức nâng cao)
- Tạo AppConfig(TypedDict) với keys: name(str), debug(bool), retries(int)
- Viết hàm validate_config(data: dict) -> AppConfig
- Nếu thiếu/kiểu sai -> ValueError
"""
from __future__ import annotations
from typing import TypedDict, Any


class AppConfig(TypedDict):
    name: str
    debug: bool
    retries: int


def validate_config(data: dict[str, Any]) -> AppConfig:
    raise NotImplementedError
