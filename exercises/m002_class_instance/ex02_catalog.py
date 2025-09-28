"""
Bài 02 (dễ) - Danh mục sản phẩm (Catalog)
Mục tiêu: Dùng class quản lý nhiều Product bằng dictionary.
Ngữ cảnh: Tạo danh mục sản phẩm của cửa hàng.

Yêu cầu triển khai lớp:
- Class Product(name, price) như bài 01 (có thể copy y hệt sang đây nếu cần)
- Class Catalog với _items: dict[str, Product]
  + add(product): thêm/ghi đè theo name
  + get(name) -> Product | None
  + to_dict() -> dict[str, dict]

Yêu cầu I/O (tự viết main):
- Input: nhiều dòng đến EOF, mỗi dòng:
  + "add name price" hoặc "get name" hoặc "dump"
- Output:
  + Với "get": in dict sản phẩm hoặc None
  + Với "dump": in dict toàn bộ danh mục
"""
from typing import Dict, Optional


class Product:
    def __init__(self, name: str, price: int) -> None:
        # write your code below
        raise NotImplementedError
        # write your code above

    def to_dict(self) -> Dict[str, int | str]:
        return {"name": self._name, "price": self._price}


class Catalog:
    def __init__(self) -> None:
        # write your code below
        raise NotImplementedError
        # write your code above

    def add(self, product: Product) -> None:
        # write your code below
        raise NotImplementedError
        # write your code above

    def get(self, name: str) -> Optional[Product]:
        # write your code below
        raise NotImplementedError
        # write your code above

    def to_dict(self) -> Dict[str, Dict[str, int | str]]:
        # write your code below
        raise NotImplementedError
        # write your code above


if __name__ == "__main__":
    # Tự viết main theo yêu cầu I/O bên trên.
    # Gợi ý:
    # - Tạo Catalog, đọc dòng lệnh tới EOF, parse và gọi phương thức
    # write your code below
    # write your code above
