"""
Bài tập: Property và validation (mức khá)
- Class Product với thuộc tính name, price (int), stock (int)
- Dùng property để kiểm soát set/get với validation
- Tạo phương thức to_dict() trả về bản sao dữ liệu
"""
from typing import Dict


class Product:
    def __init__(self, name: str, price: int, stock: int = 0) -> None:
        # TODO: dùng setter để validate
        raise NotImplementedError

    @property
    def name(self) -> str:
        raise NotImplementedError

    @name.setter
    def name(self, value: str) -> None:
        raise NotImplementedError

    @property
    def price(self) -> int:
        raise NotImplementedError

    @price.setter
    def price(self, value: int) -> None:
        raise NotImplementedError

    @property
    def stock(self) -> int:
        raise NotImplementedError

    @stock.setter
    def stock(self, value: int) -> None:
        raise NotImplementedError

    def to_dict(self) -> Dict[str, int | str]:
        raise NotImplementedError
