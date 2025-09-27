"""
Bai 17 (kho) - LRU Cache O(1)
Muc tieu: Ket hop HashMap + DoublyLinkedList de dat O(1) cho get/put.
Ngu canh: Cache voi suc chua co han, loai bo muc dung lau nhat.

Yeu cau trien khai lop:
- class LRUCache(capacity: int)
  + get(key: object) -> object | None
  + put(key: object, value: object) -> None
  + size() -> int
  + (goi y) su dung DLinkedNode(key, value) + dict map key -> node

Yeu cau I/O (tu viet main):
- Input: "new cap" | "put k v" | "get k" | "size"
"""
from __future__ import annotations
from typing import Optional


class LRUCache:
  def __init__(self, capacity: int) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above

  def get(self, key: object) -> Optional[object]:
    # write your code below
    raise NotImplementedError
    # write your code above

  def put(self, key: object, value: object) -> None:
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

