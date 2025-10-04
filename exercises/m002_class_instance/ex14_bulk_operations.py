"""
Bài 14 - Xử lý hàng loạt (Bulk Operations)
Mục tiêu: Luyện for/while loops, map, zip, multiple iterations.
Ngữ cảnh: Xử lý nhiều operations cùng lúc: batch add, apply discounts, generate reports.

PYTHON FUNDAMENTALS PRACTICE:
1. For loops: for item in items, for i in range(n)
2. While loops: while condition
3. Map function: map(lambda x: transform(x), items)
4. Zip function: zip(list1, list2) để pair items
5. Nested loops: for x in items: for y in subitems

Yêu cầu triển khai lớp:
- Class Product(name: str, price: int)
- Class Discount(percent: int)
- Class BulkProcessor
  + __init__()
  + batch_add_products(data: list[tuple[str, int]]) -> list[Product]
  + apply_discounts(products: list[Product], discounts: list[int]) -> list[int]
  + pair_products_prices(names: list[str], prices: list[int]) -> dict[str, int]
  + generate_price_table(products: list[Product], quantities: list[int]) -> list[dict]
  + apply_tiered_discount(prices: list[int]) -> list[int]  # giảm giá theo tầng

Yêu cầu I/O (tự viết main):
- Input: nhiều dòng đến EOF:
  + "batch name1,price1 name2,price2 ..." - batch add products
  + "discounts product_indices discount_percents" - apply discounts
  + "pair names prices" - pair names với prices
  + "table products quantities" - tạo bảng giá
  + "tiered prices" - áp dụng giảm giá theo tầng
- Output: tùy command
"""
from typing import List, Tuple, Dict


class Product:
    def __init__(self, name: str, price: int) -> None:
        self._name = name
        self._price = price

    def apply_discount(self, percent: int) -> int:
        """Tính giá sau giảm"""
        return self._price * (100 - percent) // 100

    def to_dict(self) -> Dict[str, int | str]:
        return {"name": self._name, "price": self._price}


class BulkProcessor:
    def __init__(self) -> None:
        # write your code below
        raise NotImplementedError
        # write your code above

    def batch_add_products(self, data: List[Tuple[str, int]]) -> List[Product]:
        """
        Tạo nhiều products cùng lúc từ list of tuples
        Gợi ý: dùng for loop hoặc list comprehension
        Input: [("Milk", 15000), ("Bread", 12000), ...]
        Output: [Product("Milk", 15000), Product("Bread", 12000), ...]
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def apply_discounts(self, products: List[Product], discounts: List[int]) -> List[int]:
        """
        Áp dụng discount % cho từng product
        Gợi ý: dùng zip() để pair product với discount
        Input: products=[p1, p2, p3], discounts=[10, 20, 15]
        Output: [discounted_price1, discounted_price2, discounted_price3]
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def pair_products_prices(self, names: List[str], prices: List[int]) -> Dict[str, int]:
        """
        Pair names với prices thành dict
        Gợi ý: dùng zip() và dict()
        Input: names=["Milk", "Bread"], prices=[15000, 12000]
        Output: {"Milk": 15000, "Bread": 12000}
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def generate_price_table(self, products: List[Product], quantities: List[int]) -> List[Dict[str, int | str]]:
        """
        Tạo bảng giá cho các quantity khác nhau
        Gợi ý: dùng nested loop hoặc list comprehension
        Input: products=[p1], quantities=[1, 2, 5]
        Output: [
            {"product": "Milk", "qty": 1, "total": 15000},
            {"product": "Milk", "qty": 2, "total": 30000},
            {"product": "Milk", "qty": 5, "total": 75000}
        ]
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def apply_tiered_discount(self, prices: List[int]) -> List[int]:
        """
        Áp dụng giảm giá theo tầng:
        - < 20000: không giảm
        - 20000-50000: giảm 5%
        - 50000-100000: giảm 10%
        - > 100000: giảm 15%
        Gợi ý: dùng for loop với if/elif/else
        """
        # write your code below
        raise NotImplementedError
        # write your code above


if __name__ == "__main__":
    """
    MINI-EXERCISES - Python Fundamentals Practice

    Exercise 1: For loop basics
    - Tạo list 10 products
    - Dùng for product in products: print(product)
    - Dùng for i in range(len(products)): print(i, products[i])

    Exercise 2: While loop
    - Tính tổng giá của products cho đến khi > 100000
    - total = 0; i = 0
    - while total <= 100000 and i < len(products):

    Exercise 3: Map function
    - Tạo list prices = [15000, 20000, 25000]
    - Apply 10% discount: list(map(lambda x: x * 0.9, prices))
    - Convert to strings: list(map(str, prices))

    Exercise 4: Zip function advanced
    - Zip 3 lists: names, prices, stocks
    - for name, price, stock in zip(names, prices, stocks):
    - Tạo dict: dict(zip(names, prices))

    Exercise 5: Nested loops
    - Matrix: products x quantities
    - for product in products:
    -     for qty in quantities:
    -         print(f"{product._name} x{qty} = {product._price * qty}")

    Exercise 6: Map + Filter + Zip combo
    - Zip products với discounts
    - Filter để chỉ lấy discounts > 10%
    - Map để tính final prices
    - Ví dụ: list(map(lambda p, d: p._price * (100-d)//100,
                      filter(lambda pd: pd[1] > 10, zip(products, discounts))))
    """
    # Tự viết main theo yêu cầu I/O bên trên.
    # Gợi ý:
    # - Tạo BulkProcessor
    # - Parse commands và gọi methods
    # write your code below
    # write your code above
