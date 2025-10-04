"""
Bài 13 - Phiên mua hàng (Shopping Session)
Mục tiêu: Luyện list operations, tuple unpacking, enumerate, history tracking.
Ngữ cảnh: Track lịch sử các actions của user, có thể undo/replay.

PYTHON FUNDAMENTALS PRACTICE:
1. List operations: append(), pop(), insert(), remove()
2. Tuple unpacking: action, data = history_item
3. Enumerate: for i, item in enumerate(list)
4. List slicing: list[:n], list[-n:]
5. Tuple creation: (action, timestamp, data)

Yêu cầu triển khai lớp:
- Class Product(name: str, price: int)
- Class ShoppingSession
  + __init__()
  + add_to_cart(product: Product, qty: int) -> None
  + remove_from_cart(product_name: str, qty: int) -> None
  + view_product(product: Product) -> None
  + undo_last() -> tuple | None  # trả về action bị undo
  + get_history(limit: int = 10) -> list[tuple]  # lấy N actions gần nhất
  + replay() -> list[str]  # replay tất cả actions
  + clear_history() -> None

Yêu cầu I/O (tự viết main):
- Input: nhiều dòng đến EOF:
  + "add product_name price qty" - thêm vào cart
  + "remove product_name qty" - xóa khỏi cart
  + "view product_name price" - xem sản phẩm
  + "undo" - undo action cuối cùng
  + "history n" - xem n actions gần nhất
  + "replay" - replay tất cả actions
  + "clear" - xóa history
- Output: tùy command
"""
from typing import List, Tuple, Optional
from datetime import datetime


class Product:
    def __init__(self, name: str, price: int) -> None:
        self._name = name
        self._price = price

    def to_dict(self) -> dict:
        return {"name": self._name, "price": self._price}


class ShoppingSession:
    def __init__(self) -> None:
        """
        Khởi tạo history để lưu các actions
        Gợi ý: _history: list[tuple[str, str, dict]]
        Mỗi tuple: (action_type, timestamp, data)
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def add_to_cart(self, product: Product, qty: int) -> None:
        """
        Thêm product vào cart và log vào history
        Gợi ý: _history.append(("add", timestamp, {"product": ..., "qty": ...}))
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def remove_from_cart(self, product_name: str, qty: int) -> None:
        """
        Xóa product khỏi cart và log vào history
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def view_product(self, product: Product) -> None:
        """
        Log việc xem sản phẩm
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def undo_last(self) -> Optional[Tuple[str, str, dict]]:
        """
        Undo action cuối cùng
        Gợi ý: dùng list.pop() nếu history không rỗng
        Trả về tuple của action bị undo, hoặc None
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def get_history(self, limit: int = 10) -> List[Tuple[str, str, dict]]:
        """
        Lấy n actions gần nhất
        Gợi ý: dùng list slicing _history[-limit:]
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def replay(self) -> List[str]:
        """
        Replay tất cả actions thành list strings
        Gợi ý: dùng enumerate và format string
        Ví dụ: ["0: add Milk x2 at 2024-01-01 10:00", ...]
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def clear_history(self) -> None:
        """
        Xóa toàn bộ history
        Gợi ý: _history.clear() hoặc _history = []
        """
        # write your code below
        raise NotImplementedError
        # write your code above


if __name__ == "__main__":
    """
    MINI-EXERCISES - Python Fundamentals Practice

    Exercise 1: List operations
    - Tạo list 10 actions (tuples)
    - Practice: append, insert(0, item), pop(), pop(0), remove()
    - In list sau mỗi operation

    Exercise 2: Tuple unpacking
    - Tạo list of tuples: [(action, time, data), ...]
    - Dùng for action, time, data in history:
    - In từng phần tử riêng biệt

    Exercise 3: Enumerate
    - Dùng enumerate để in history với index
    - for i, (action, time, data) in enumerate(history, start=1):
    - Format: "Action #1: add at 10:00"

    Exercise 4: List slicing advanced
    - Lấy 5 actions đầu: history[:5]
    - Lấy 5 actions cuối: history[-5:]
    - Lấy mỗi action thứ 2: history[::2]
    - Reverse list: history[::-1]

    Exercise 5: List filtering with enumerate
    - Tìm index của action "add" đầu tiên
    - Tìm tất cả indices của actions "remove"
    - Dùng: [i for i, (act, _, _) in enumerate(history) if act == "remove"]
    """
    # Tự viết main theo yêu cầu I/O bên trên.
    # Gợi ý:
    # - Tạo ShoppingSession
    # - Parse commands và gọi methods
    # - Format timestamp: datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # write your code below
    # write your code above
