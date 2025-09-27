"""
Bai 05 (vua) - Danh sach lien ket don (Singly Linked List)
Muc tieu: Luyen tap Node, tham chieu next, duyet va thao tac co ban.
Ngu canh: Xay dung LinkedList don gian.

Yeu cau trien khai lop:
- class Node(value: object)
  + value: object
  + next: Node | None
- class SinglyLinkedList
  + append(x) -> None
  + prepend(x) -> None
  + insert_at(index: int, x) -> bool
  + remove_value(x) -> bool
  + find(x) -> int | None  (tra ve index dau tien)
  + to_list() -> list[object]

Yeu cau I/O (tu viet main):
- Input: lenh "append x" | "prepend x" | "insert i x" | "remove x" | "find x" | "dump"
- Output: voi find -> in index hoac None, dump -> in list
"""
from __future__ import annotations
from typing import Optional, List


class Node:
  def __init__(self, value: object) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above


class SinglyLinkedList:
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

  def remove_value(self, x: object) -> bool:
    # write your code below
    raise NotImplementedError
    # write your code above

  def find(self, x: object) -> Optional[int]:
    # write your code below
    raise NotImplementedError
    # write your code above

  def to_list(self) -> List[object]:
    # write your code below
    raise NotImplementedError
    # write your code above


if __name__ == "__main__":
  # Tu viet main theo yeu cau I/O ben tren.
  # write your code below
  # write your code above

