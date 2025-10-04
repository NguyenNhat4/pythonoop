"""
Bài 12 - Quản lý danh mục (Category Manager)
Mục tiêu: Luyện dict operations, set operations, dict iteration.
Ngữ cảnh: Quản lý sản phẩm theo categories, tìm sản phẩm chung giữa các categories.

PYTHON FUNDAMENTALS PRACTICE:
1. Dict operations: get(), setdefault(), items(), keys(), values()
2. Set operations: add(), union(), intersection(), difference()
3. Dict iteration: for key, value in dict.items()
4. Dict comprehension: {k: v for k, v in items}
5. Set comprehension: {x for x in items}

Yêu cầu triển khai lớp:
- Class Product(name: str, price: int)
- Class CategoryManager
  + __init__()
  + add_to_category(category: str, product: Product) -> None
  + get_products(category: str) -> set[Product]
  + get_all_categories() -> list[str]
  + get_common_products(cat1: str, cat2: str) -> set[Product]
  + merge_categories(cat1: str, cat2: str, new_name: str) -> None
  + remove_from_category(category: str, product_name: str) -> None
  + count_by_category() -> dict[str, int]

Yêu cầu I/O (tự viết main):
- Input: nhiều dòng đến EOF:
  + "add category product_name price" - thêm sản phẩm vào category
  + "get category" - lấy tất cả products trong category
  + "common cat1 cat2" - tìm products chung giữa 2 categories
  + "merge cat1 cat2 new_name" - merge 2 categories thành 1
  + "remove category product_name" - xóa product khỏi category
  + "count" - đếm số products trong mỗi category
  + "categories" - list tất cả categories
- Output: tùy command, in list/dict/set phù hợp
"""
from typing import Dict, List, Set


class Product:
    def __init__(self, name: str, price: int) -> None:
        self._name = name
        self._price = price

    def __eq__(self, other: object) -> bool:
        """So sánh 2 products dựa trên name"""
        if not isinstance(other, Product):
            return False
        return self._name == other._name

    def __hash__(self) -> int:
        """Để có thể dùng Product trong set"""
        return hash(self._name)

    def to_dict(self) -> Dict[str, int | str]:
        return {"name": self._name, "price": self._price}


class CategoryManager:
    def __init__(self) -> None:
        """
        Khởi tạo dict để lưu categories
        Gợi ý: _categories: dict[str, set[Product]]
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def add_to_category(self, category: str, product: Product) -> None:
        """
        Thêm product vào category
        Gợi ý: dùng setdefault() để tạo set nếu chưa có
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def get_products(self, category: str) -> Set[Product]:
        """
        Lấy tất cả products trong category
        Gợi ý: dùng get() với default value là empty set
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def get_all_categories(self) -> List[str]:
        """
        Lấy list tất cả categories
        Gợi ý: dùng dict.keys() và convert sang list
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def get_common_products(self, cat1: str, cat2: str) -> Set[Product]:
        """
        Tìm products có trong cả 2 categories
        Gợi ý: dùng set intersection (&)
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def merge_categories(self, cat1: str, cat2: str, new_name: str) -> None:
        """
        Merge 2 categories thành 1 category mới
        Gợi ý: dùng set union (|), rồi xóa 2 categories cũ
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def remove_from_category(self, category: str, product_name: str) -> None:
        """
        Xóa product khỏi category
        Gợi ý: tìm product theo name, dùng set.discard()
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def count_by_category(self) -> Dict[str, int]:
        """
        Đếm số products trong mỗi category
        Gợi ý: dùng dict comprehension {cat: len(products) for ...}
        """
        # write your code below
        raise NotImplementedError
        # write your code above


if __name__ == "__main__":
    """
    MINI-EXERCISES - Python Fundamentals Practice

    Exercise 1: Dict operations
    - Tạo dict với 3 categories, mỗi category có 3-5 products
    - Dùng setdefault() để add products
    - In dict.keys(), dict.values(), dict.items()

    Exercise 2: Set operations
    - Tạo 3 sets: electronics, books, clothing
    - Tìm union (tất cả), intersection (chung), difference (khác)
    - Gợi ý: set1 | set2, set1 & set2, set1 - set2

    Exercise 3: Dict & Set comprehension
    - Tạo dict mapping category -> total price
    - Dùng: {cat: sum(p._price for p in products) for cat, products in ...}
    - Tạo set tất cả product names: {p._name for products in ... for p in products}

    Exercise 4: Advanced filtering
    - Tìm categories có > 3 products
    - Tìm categories có tổng giá > 100000
    - Dùng dict comprehension với condition
    """
    # Tự viết main theo yêu cầu I/O bên trên.
    # Gợi ý:
    # - Tạo CategoryManager
    # - Parse commands và gọi methods
    # - Convert set[Product] thành list[dict] để in
    # write your code below
    # write your code above
