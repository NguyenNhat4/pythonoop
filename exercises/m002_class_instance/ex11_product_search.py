"""
Bài 11 - Tìm kiếm và lọc sản phẩm (Product Search & Filter)
Mục tiêu: Luyện list comprehension, filter, sorted, lambda.
Ngữ cảnh: Tìm kiếm sản phẩm theo nhiều điều kiện khác nhau.

PYTHON FUNDAMENTALS PRACTICE:
1. List comprehension: [x for x in items if condition]
2. Built-in filter(): filter(lambda x: condition, items)
3. Built-in sorted(): sorted(items, key=lambda x: x.attr)
4. Lambda functions: lambda x: expression
5. Multiple conditions: and, or, not

Yêu cầu triển khai lớp:
- Class Product(name: str, price: int, category: str, stock: int)
  + to_dict() -> dict
- Class ProductFilter
  + __init__(products: list[Product])
  + by_price_range(min_price, max_price) -> list[Product]
  + by_category(category: str) -> list[Product]
  + in_stock() -> list[Product]
  + sort_by_price(ascending=True) -> list[Product]
  + search_by_name(keyword: str) -> list[Product]

Yêu cầu I/O (tự viết main):
- Input: nhiều dòng đến EOF:
  + "add name price category stock" - thêm sản phẩm
  + "price min max" - lọc theo giá
  + "category cat_name" - lọc theo category
  + "stock" - chỉ lấy có hàng
  + "sort asc/desc" - sắp xếp theo giá
  + "search keyword" - tìm theo tên (partial match, case-insensitive)
- Output: in list dict của các sản phẩm tìm được
"""
from typing import Dict, List


class Product:
    def __init__(self, name: str, price: int, category: str, stock: int) -> None:
        # write your code below
        raise NotImplementedError
        # write your code above

    def to_dict(self) -> Dict[str, int | str]:
        # write your code below
        raise NotImplementedError
        # write your code above


class ProductFilter:
    def __init__(self, products: List[Product]) -> None:
        # write your code below
        raise NotImplementedError
        # write your code above

    def by_price_range(self, min_price: int, max_price: int) -> List[Product]:
        """
        Lọc sản phẩm trong khoảng giá [min_price, max_price]
        Gợi ý: dùng list comprehension
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def by_category(self, category: str) -> List[Product]:
        """
        Lọc sản phẩm theo category
        Gợi ý: dùng list comprehension hoặc filter()
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def in_stock(self) -> List[Product]:
        """
        Chỉ lấy sản phẩm còn hàng (stock > 0)
        Gợi ý: dùng filter() với lambda
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def sort_by_price(self, ascending: bool = True) -> List[Product]:
        """
        Sắp xếp sản phẩm theo giá
        Gợi ý: dùng sorted() với key=lambda
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def search_by_name(self, keyword: str) -> List[Product]:
        """
        Tìm sản phẩm có tên chứa keyword (không phân biệt hoa thường)
        Gợi ý: dùng str.lower() và 'in' operator
        """
        # write your code below
        raise NotImplementedError
        # write your code above


if __name__ == "__main__":
    """
    MINI-EXERCISES - Python Fundamentals Practice

    Exercise 1: List Comprehension
    - Tạo list 10 products với giá ngẫu nhiên
    - Dùng list comprehension lọc products có giá > 50000

    Exercise 2: Filter & Lambda
    - Dùng filter() để lọc products có stock > 5
    - Dùng lambda function

    Exercise 3: Sorted với multiple keys
    - Sort theo category, rồi theo price
    - Gợi ý: key=lambda x: (x.category, x.price)

    Exercise 4: Combine filters
    - Lọc products: category='Electronics' AND price < 100000 AND stock > 0
    - Có thể chain các methods hoặc dùng multiple conditions
    """
    # Tự viết main theo yêu cầu I/O bên trên.
    # Gợi ý:
    # - Tạo ProductFilter với empty list
    # - Parse commands và gọi methods tương ứng
    # - In kết quả dưới dạng list of dicts
    # write your code below
    # write your code above
