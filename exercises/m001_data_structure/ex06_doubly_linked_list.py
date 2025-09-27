"""
Bai 06 (vua-kha) - Danh sach lien ket kep (Doubly Linked List)
Muc tieu: Luyen tap next/prev, chen/xoa o giua, dao nguoc danh sach.
Ngu canh: Mo rong tu singly sang doubly.

Yeu cau trien khai lop:
- class DNode(value: object)
  + value: object
  + prev: DNode | None
  + next: DNode | None
- class DoublyLinkedList
  + append(x) -> None
  + prepend(x) -> None
  + insert_at(index: int, x) -> bool
  + remove_at(index: int) -> bool
  + reverse() -> None
  + to_list_forward() -> list[object]
  + to_list_backward() -> list[object]

Yeu cau I/O (tu viet main):
- Input: "append x" | "prepend x" | "insert i x" | "remove i" | "reverse" | "dump f" | "dump b"
"""
from __future__ import annotations
from typing import Optional, List


class DNode:
  def __init__(self, value: object) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above


class DoublyLinkedList:
  def __init__(self) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above

  def append(self, x: object) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above

  def prepend(self, x: object) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above

  def insert_at(self, index: int, x: object) -> bool:
    # write your code below
    raise NotImplementedError
    # write your code above

  def remove_at(self, index: int) -> bool:
    # write your code below
    raise NotImplementedError
    # write your code above

  def reverse(self) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above

  def to_list_forward(self) -> List[object]:
    # write your code below
    raise NotImplementedError
    # write your code above

  def to_list_backward(self) -> List[object]:
    # write your code below
    raise NotImplementedError
    # write your code above


if __name__ == "__main__":
  # Tu viet main theo yeu cau I/O ben tren.
  # write your code below
  # write your code above

