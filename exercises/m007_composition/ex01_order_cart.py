"""
Bài tập: Composition (mức khá-nâng cao)
- Class Item(name, price)
- Class Cart chứa nhiều Item và có method add(item), total()
- Không lộ cấu trúc list nội bộ; to_dict() để xuất dữ liệu
"""
from typing import Dict, List


class Item:
    def __init__(self, name: str, price: int) -> None:
        # TODO: validate
        raise NotImplementedError

    def to_dict(self) -> Dict[str, int | str]:
        raise NotImplementedError


class Cart:
    def __init__(self) -> None:
        # TODO: danh sách items private
        raise NotImplementedError

    def add(self, item: Item) -> None:
        # TODO: thêm item
        raise NotImplementedError

    def total(self) -> int:
        # TODO: tính tổng
        raise NotImplementedError

    def to_dict(self) -> Dict[str, List[Dict[str, int | str]]]:
        raise NotImplementedError
