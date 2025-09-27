"""
Bai 11 (kha) - Heap nhi phan (Binary Heap)
Muc tieu: Trien khai min-heap hoac max-heap voi mang; sift up/down.
Ngu canh: Quan ly thu tu uu tien co ban.

Yeu cau trien khai lop:
- class BinaryHeap(min_heap: bool = True)
  + push(x: int) -> None
  + pop() -> int | None
  + peek() -> int | None
  + size() -> int
  + (goi y) _sift_up(i), _sift_down(i)

Yeu cau I/O (tu viet main):
- Input: "push x" | "pop" | "peek" | "size" (co the them "mode min|max")
"""
from typing import List, Optional


class BinaryHeap:
  def __init__(self, min_heap: bool = True) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above

  def push(self, x: int) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above

  def pop(self) -> Optional[int]:
    # write your code below
    raise NotImplementedError
    # write your code above

  def peek(self) -> Optional[int]:
    # write your code below
    raise NotImplementedError
    # write your code above

  def size(self) -> int:
    # write your code below
    raise NotImplementedError
    # write your code above

  def _sift_up(self, i: int) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above

  def _sift_down(self, i: int) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above


if __name__ == "__main__":
  # Tu viet main theo yeu cau I/O ben tren.
  # write your code below
  # write your code above

