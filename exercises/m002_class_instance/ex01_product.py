"""
Bài 01 - Sản phẩm trong cửa hàng (Product)
Mục tiêu: Làm quen với class & instance, thuộc tính cơ bản.
Ngữ cảnh: Lưu thông tin một sản phẩm đơn giản.

Yêu cầu triển khai lớp:
- Class Product(name: str, price: int)
  + name: tên sản phẩm (không rỗng)
  + price: đơn giá (đơn vị: đồng, >= 0)
- to_dict() -> dict[str, int|str]

Yêu cầu I/O (tự viết main):
- Input:
  Dòng 1: tên sản phẩm
  Dòng 2: đơn giá (số nguyên)
- Output: in dict thông tin sản phẩm, ví dụ: {'name': 'Milk', 'price': 15000}
"""
from typing import Dict


class Product:
    def __init__(self, name: str, price: int) -> None:
        # write your code below
        # write your code above
        raise NotImplementedError
        

    def to_dict(self) -> Dict[str, int | str]:
        # write your code below
        # write your code above
        raise NotImplementedError
        


if __name__ == "__main__":
    """
    MINI-EXERCISES - Python Fundamentals Practice

    Exercise 1: List operations with Products
    - Tạo list 5 products với giá khác nhau
    - Sort theo giá: sorted(products, key=lambda p: p._price)
    - In tên của product đắt nhất và rẻ nhất
    - Gợi ý: max(products, key=lambda p: p._price)._name

    Exercise 2: List comprehension
    - Tạo list products
    - Lọc products có giá > 20000: [p for p in products if p._price > 20000]
    - Tạo list chỉ chứa tên: [p._name for p in products]
    - Tạo list prices: [p._price for p in products]

    Exercise 3: Aggregations
    - Tính tổng giá tất cả products: sum(p._price for p in products)
    - Tính giá trung bình: sum(prices) / len(prices)
    - Đếm products có giá < 15000: sum(1 for p in products if p._price < 15000)

    Exercise 4: Dict operations
    - Convert list products thành dict: {p._name: p._price for p in products}
    - Group products theo price ranges:
      cheap (< 15000), medium (15000-30000), expensive (> 30000)
    - Gợi ý: dùng defaultdict(list) hoặc dict với loops

    Exercise 5: String formatting
    - In products theo format: "Milk: 15,000đ"
    - Dùng f-string: f"{p._name}: {p._price:,}đ"
    - Sort và in theo thứ tự alphabet
    """
    # Tự viết main theo yêu cầu I/O bên trên.
    # Gợi ý:
    # - Đọc name, price
    # - p = Product(name, price); print(p.to_dict())
    # write your code below
    # write your code above
