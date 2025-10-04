"""
Bài 02 - Danh mục sản phẩm (Catalog)
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
    """
    MINI-EXERCISES - Python Fundamentals Practice

    Exercise 1: Dict operations basics
    - Tạo Catalog và add 5 products
    - Practice: catalog._items.keys(), .values(), .items()
    - Check if product exists: "Milk" in catalog._items
    - Get with default: catalog._items.get("XYZ", None)

    Exercise 2: Dict iteration
    - Iterate dict: for name, product in catalog._items.items():
    - Print: f"{name}: {product._price:,}đ"
    - Get list of names: list(catalog._items.keys())
    - Get list of prices: [p._price for p in catalog._items.values()]

    Exercise 3: Dict comprehension
    - Tạo dict giá > 20000: {k: v for k, v in items.items() if v._price > 20000}
    - Tạo dict name -> price: {k: v._price for k, v in items.items()}
    - Reverse dict: {v._price: k for k, v in items.items()}

    Exercise 4: Batch operations
    - Load products từ list of tuples: [("Milk", 15000), ("Bread", 12000), ...]
    - Dùng for loop để add tất cả vào catalog
    - Dùng dict comprehension để tạo price_map

    Exercise 5: Search & filter
    - Search by partial name: [p for p in catalog._items.values() if "milk" in p._name.lower()]
    - Filter by price range: {k: v for k, v in items.items() if 10000 <= v._price <= 20000}
    - Sort by name: dict(sorted(items.items()))
    - Sort by price: dict(sorted(items.items(), key=lambda x: x[1]._price))

    Exercise 6: Export formats
    - Export as list of dicts: [p.to_dict() for p in catalog._items.values()]
    - Export as list of tuples: [(k, v._price) for k, v in items.items()]
    - Export as CSV string: "\\n".join(f"{k},{v._price}" for k, v in items.items())
    """
    # Tự viết main theo yêu cầu I/O bên trên.
    # Gợi ý:
    # - Tạo Catalog, đọc dòng lệnh tới EOF, parse và gọi phương thức
    # write your code below
    # write your code above
