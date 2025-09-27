"""
Bai 12 (kha) - Hang doi uu tien (Priority Queue) tren nen Heap
Muc tieu: Dong goi heap thanh PriorityQueue; lam viec voi (priority, item).
Ngu canh: Quan ly item theo do uu tien tang dan (min-heap).

Yeu cau trien khai lop:
- class PriorityQueue
  + push(item: object, priority: int) -> None
  + pop() -> tuple[int, object] | None
  + peek() -> tuple[int, object] | None
  + size() -> int

Yeu cau I/O (tu viet main):
- Input: "push item p" | "pop" | "peek" | "size"
"""
from typing import Optional, Tuple


class PriorityQueue:
  def __init__(self) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above

  def push(self, item: object, priority: int) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above

  def pop(self) -> Optional[Tuple[int, object]]:
    # write your code below
    raise NotImplementedError
    # write your code above

  def peek(self) -> Optional[Tuple[int, object]]:
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

