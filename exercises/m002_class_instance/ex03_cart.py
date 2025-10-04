"""
Bài 03 - Giỏ hàng cơ bản (Cart)
Mục tiêu: Dùng class chứa state, thao tác với Product.
Ngữ cảnh: Thêm sản phẩm vào giỏ và xem tổng tiền.

Yêu cầu triển khai lớp:
- Class Product(name, price) như bài 01
- Class Cart với _items: dict[str, int] (map name -> quantity)
  + add(product: Product, qty: int)
  + remove(name: str, qty: int)
  + total(catalog: Catalog) -> int (tính theo price trong Catalog)

Yêu cầu I/O (tự viết main):
- Input: nhiều dòng đến EOF, mỗi dòng:
  + "add name qty" | "remove name qty" | "total"
- Output:
  + Với "total": in tổng tiền (int)
"""
from __future__ import annotations
from typing import Dict


class Product:
    def __init__(self, name: str, price: int) -> None:
        self._name = name
        self._price = price 


class Catalog:
    def __init__(self) -> None:
        self._items: Dict[str, Product] = {}

    def add(self, product: Product) -> None:
        self._items[product._name] = product

    def get(self, name: str) -> Product | None:
        return self._items.get(name)
        
    def to_dict(self) -> Dict[str, Product]:
        return {name: product.to_dict() for name, product in self._items.items()}

class Cart:
    def __init__(self) -> None:
        # write your code below
        self._items: Dict[str, Product] = {}
        # write your code above

    def add(self, product: Product, qty: int) -> None:
        # write your code below
        self._items[product._name] = product
        # write your code above

    def remove(self, name: str, qty: int) -> None:
        # write your code below
        self._items[name] -= qty
        # write your code above

    def total(self, catalog: Catalog) -> int:
        # write your code below
        return sum(product.price * qty for product, qty in self._items.items())
        # write your code above


if __name__ == "__main__":
    """
    MINI-EXERCISES - Python Fundamentals Practice

    Exercise 1: Dict với quantity management
    - Cart lưu: {product_name: quantity}
    - Practice: dict.setdefault(), dict.get()
    - Add quantity: cart[name] = cart.get(name, 0) + qty
    - Remove quantity: cart[name] = max(0, cart.get(name, 0) - qty)

    Exercise 2: Calculate totals
    - Tính total từ cart dict và catalog
    - for name, qty in cart.items():
    -     product = catalog.get(name)
    -     total += product._price * qty
    - Dùng sum với generator: sum(catalog.get(n)._price * q for n, q in cart.items())

    Exercise 3: Merge carts
    - Merge 2 cart dicts thành 1
    - for name, qty in cart2.items():
    -     cart1[name] = cart1.get(name, 0) + qty
    - Hoặc dùng Counter: from collections import Counter; Counter(cart1) + Counter(cart2)

    Exercise 4: Discount rules
    - Apply discount nếu total > threshold
    - if total >= 100000: discount = total * 10 // 100
    - Tiered discount: [(50000, 5), (100000, 10), (200000, 15)]
    - for threshold, percent in tiers:
    -     if total >= threshold: discount_percent = percent

    Exercise 5: Group items by price threshold
    - Chia items thành expensive (> 20000) và cheap (<= 20000)
    - expensive = {k: v for k, v in cart.items() if catalog.get(k)._price > 20000}
    - cheap = {k: v for k, v in cart.items() if catalog.get(k)._price <= 20000}

    Exercise 6: Cart statistics
    - Total items: sum(cart.values())
    - Unique products: len(cart)
    - Most quantity: max(cart.items(), key=lambda x: x[1])
    - Average quantity: sum(cart.values()) / len(cart)
    """
    # Tự viết main theo yêu cầu I/O bên trên.
    # Gợi ý:
    # - Tạo Catalog, thêm vài Product mẫu (tuỳ bạn)
    # - Tạo Cart, xử lý lệnh add/remove/total
    # write your code below
    # write your code above
