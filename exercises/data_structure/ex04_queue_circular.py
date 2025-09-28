"""
Bai 04 (de-vua) - Hang doi vong (Circular Queue)
Muc tieu: Quan ly bo nho va chi so vong (head/tail), trang thai full/empty.
Ngu canh: Trien khai queue co suc chua co dinh.

Yeu cau trien khai lop:
- Class CircularQueue(capacity: int)
  + enqueue(x: object) -> bool  (True neu thanh cong, False neu full)
  + dequeue() -> object | None  (None neu empty)
  + front() -> object | None
  + rear() -> object | None
  + is_empty() -> bool
  + is_full() -> bool
  + size() -> int

Yeu cau I/O (tu viet main):
- Input: "new cap" de tao queue, sau do: "enq x" | "deq" | "front" | "rear" | "size" | "empty" | "full"
- Output: in ket qua cac lenh truy van
"""
from typing import List, Optional


class CircularQueue:
  def __init__(self, capacity: int) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above

  def enqueue(self, x: object) -> bool:
    # write your code below
    raise NotImplementedError
    # write your code above

  def dequeue(self) -> Optional[object]:
    # write your code below
    raise NotImplementedError
    # write your code above

  def front(self) -> Optional[object]:
    # write your code below
    raise NotImplementedError
    # write your code above

  def rear(self) -> Optional[object]:
    # write your code below
    raise NotImplementedError
    # write your code above

  def is_empty(self) -> bool:
    # write your code below
    raise NotImplementedError
    # write your code above

  def is_full(self) -> bool:
    # write your code below
    raise NotImplementedError
    # write your code above

  def size(self) -> int:
    # write your code below
    raise NotImplementedError
    # write your code above


if __name__ == "__main__":
  # Tu viet main theo yeu cau I/O ben tren.
  # write your code below
  # write your code above

