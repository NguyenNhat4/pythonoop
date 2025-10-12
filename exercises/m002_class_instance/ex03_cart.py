"""
Bài 03 - Giỏ hàng cơ bản (Cart)
Mục tiêu: Dùng class chứa state, thao tác với Product và Catalog.
Ngữ cảnh: Thêm sản phẩm vào giỏ và tính tổng tiền.

PYTHON FUNDAMENTALS PRACTICE:
1. Dict operations: get(), keys(), values(), items()
2. Dict update: dict[key] = value, dict[key] += value
3. Iteration: for key, value in dict.items()
4. Conditional operations: if key in dict
5. Default values: dict.get(key, default)

YÊU CẦU HỌC TRƯỚC:
- Đã hoàn thành ex01_product.py
- Đã hoàn thành ex02_catalog.py
- Hiểu về dict operations

Yêu cầu triển khai lớp:
- Class Product(name, price) như bài 01
- Class Cart với _items: dict[str, int] (map name -> quantity)
  + add(product: Product, qty: int) - thêm sản phẩm vào giỏ
  + remove(name: str, qty: int) - xóa/giảm số lượng sản phẩm
  + total(catalog: Catalog) -> int - tính tổng tiền (lấy giá từ Catalog)
  + get_items() -> Dict[str, int] - xem giỏ hàng
  + clear() - xóa toàn bộ giỏ hàng

Yêu cầu I/O (tự viết main):
- Input: nhiều dòng đến EOF, mỗi dòng:
  + "add name qty" - thêm sản phẩm vào giỏ
  + "remove name qty" - xóa/giảm số lượng
  + "total" - in tổng tiền
  + "dump" - in giỏ hàng (dict name -> qty)
  + "clear" - xóa toàn bộ giỏ
- Output:
  + Với "total": in tổng tiền (int)
  + Với "dump": in dict giỏ hàng
"""
from __future__ import annotations
from typing import Dict
from ex02_catalog import Catalog, Product


class Cart:
    def __init__(self) -> None:
        """
        Khởi tạo giỏ hàng rỗng
        _items: dict[str, int] lưu tên sản phẩm -> số lượng
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def add(self, product: Product, qty: int) -> None:
        """
        Thêm sản phẩm vào giỏ

        Args:
            product: Product object
            qty: số lượng (phải > 0)

        Logic:
        - Nếu sản phẩm đã có trong giỏ: cộng thêm số lượng
        - Nếu chưa có: thêm mới với số lượng qty
        - Nếu qty <= 0: không làm gì

        Gợi ý:
        - Lấy tên: product._name hoặc product.to_dict()['name']
        - Check: if name in self._items
        - Update: self._items[name] = self._items.get(name, 0) + qty

        Example:
            cart = Cart()
            cart.add(Product("Milk", 15000), 2)
            cart.add(Product("Milk", 15000), 1)  # Tổng 3 Milk
            # cart._items = {"milk": 3}
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def remove(self, name: str, qty: int) -> None:
        """
        Xóa hoặc giảm số lượng sản phẩm trong giỏ

        Args:
            name: tên sản phẩm (case-insensitive)
            qty: số lượng cần xóa (phải > 0)

        Logic:
        - Nếu sản phẩm không có trong giỏ: không làm gì
        - Nếu qty >= số lượng hiện tại: xóa sản phẩm khỏi giỏ
        - Nếu qty < số lượng hiện tại: giảm số lượng

        Gợi ý:
        - name = name.lower()
        - current_qty = self._items.get(name, 0)
        - if current_qty <= qty: del self._items[name]
        - else: self._items[name] -= qty

        Example:
            cart._items = {"milk": 5}
            cart.remove("Milk", 2)  # {"milk": 3}
            cart.remove("Milk", 10) # {} (xóa hết)
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def total(self, catalog: Catalog) -> int:
        """
        Tính tổng tiền giỏ hàng

        Args:
            catalog: Catalog object để lấy giá sản phẩm

        Returns:
            Tổng tiền (int)

        Logic:
        - Duyệt qua từng item trong giỏ
        - Lấy giá từ catalog: product = catalog.search_by_name(name)
        - Nếu sản phẩm không tồn tại trong catalog: bỏ qua (hoặc giá = 0)
        - Tính: tổng += giá * số lượng

        Gợi ý:
        total = 0
        for name, qty in self._items.items():
            product = catalog.search_by_name(name)
            if product:
                total += product._price * qty
        return total

        Example:
            catalog có: Milk (15000), Bread (12000)
            cart._items = {"milk": 2, "bread": 1}
            cart.total(catalog) = 15000*2 + 12000*1 = 42000
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def get_items(self) -> Dict[str, int]:
        """
        Lấy dict giỏ hàng (name -> quantity)

        Returns:
            Copy của _items để tránh modify từ bên ngoài

        Gợi ý:
        - return self._items.copy()
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def clear(self) -> None:
        """
        Xóa toàn bộ giỏ hàng

        Gợi ý:
        - self._items.clear() hoặc self._items = {}
        """
        # write your code below
        raise NotImplementedError
        # write your code above


if __name__ == "__main__":
    """
    MINI-EXERCISES - Python Fundamentals Practice

    Exercise 1: Dict basic operations
    - Tạo dict items = {"milk": 2, "bread": 3}
    - Add new: items["cheese"] = 1
    - Update: items["milk"] += 2
    - Remove: del items["bread"]
    - Check: if "milk" in items

    Exercise 2: Dict iteration
    - items = {"milk": 2, "bread": 3, "cheese": 1}
    - for name in items.keys(): print(name)
    - for qty in items.values(): print(qty)
    - for name, qty in items.items(): print(f"{name}: {qty}")

    Exercise 3: Dict aggregation
    - items = {"milk": 2, "bread": 3, "cheese": 1}
    - prices = {"milk": 15000, "bread": 12000, "cheese": 8000}
    - Tính total: sum(prices[name] * qty for name, qty in items.items())

    Exercise 4: Dict with default values
    - items = {}
    - items["milk"] = items.get("milk", 0) + 1  # Add 1
    - items["milk"] = items.get("milk", 0) + 2  # Add 2 more -> total 3

    Exercise 5: Dict merge operations
    - cart1 = {"milk": 2, "bread": 3}
    - cart2 = {"milk": 1, "cheese": 2}
    - Merge: for item, qty in cart2.items():
    -           cart1[item] = cart1.get(item, 0) + qty
    - Result: {"milk": 3, "bread": 3, "cheese": 2}
    """

    # Tự viết main theo yêu cầu I/O bên trên.
    # Gợi ý:
    # - Tạo Catalog, thêm vài Product mẫu (tuỳ bạn)
    # - Tạo Cart, xử lý lệnh add/remove/total/dump/clear
    # write your code below

    # VÍ DỤ SETUP:
    # Tạo catalog với một số products
    catalog = Catalog()
    catalog.add(Product("Milk", 15000))
    catalog.add(Product("Bread", 12000))
    catalog.add(Product("Cheese", 8000))
    catalog.add(Product("Butter", 25000))

    # Tạo cart
    cart = Cart()

    # TEST CODE (uncomment sau khi implement):
    print("=== TEST CART ===")

    # Test add
    # cart.add(Product("Milk", 15000), 2)
    # cart.add(Product("Bread", 12000), 1)
    # print("After adding:", cart.get_items())
    # # Expected: {"milk": 2, "bread": 1}

    # Test add existing product
    # cart.add(Product("Milk", 15000), 1)
    # print("After adding more milk:", cart.get_items())
    # # Expected: {"milk": 3, "bread": 1}

    # Test remove
    # cart.remove("milk", 1)
    # print("After removing 1 milk:", cart.get_items())
    # # Expected: {"milk": 2, "bread": 1}

    # Test total
    # total = cart.total(catalog)
    # print(f"Total: {total:,}đ")
    # # Expected: 15000*2 + 12000*1 = 42000

    # Test clear
    # cart.clear()
    # print("After clear:", cart.get_items())
    # # Expected: {}

    # I/O PROCESSING:
    # while True:
    #     try:
    #         line = input().strip().split()
    #         command = line[0]
    #
    #         if command == "add":
    #             name, qty = line[1], int(line[2])
    #             product = catalog.search_by_name(name)
    #             if product:
    #                 cart.add(product, qty)
    #         elif command == "remove":
    #             name, qty = line[1], int(line[2])
    #             cart.remove(name, qty)
    #         elif command == "total":
    #             print(cart.total(catalog))
    #         elif command == "dump":
    #             print(cart.get_items())
    #         elif command == "clear":
    #             cart.clear()
    #     except EOFError:
    #         break

    # write your code above
