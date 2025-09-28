"""
Bai 13 (kha) - Cay nhi phan tim kiem (BST)
Muc tieu: Them/xoa/tim kiem; duyet inorder/preorder/postorder; min/max/height.
Ngu canh: Xay dung BST co ban.

Yeu cau trien khai lop:
- class BSTNode(key: int)
  + key: int
  + left: BSTNode | None
  + right: BSTNode | None
- class BinarySearchTree
  + insert(k: int) -> None
  + find(k: int) -> bool
  + delete(k: int) -> bool
  + inorder() -> list[int]
  + preorder() -> list[int]
  + postorder() -> list[int]
  + min() -> int | None
  + max() -> int | None
  + height() -> int

Yeu cau I/O (tu viet main):
- Input: "ins k" | "find k" | "del k" | "in" | "pre" | "post" | "min" | "max" | "h"
"""
from __future__ import annotations
from typing import Optional, List


class BSTNode:
  def __init__(self, key: int) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above


class BinarySearchTree:
  def __init__(self) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above

  def insert(self, k: int) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above

  def find(self, k: int) -> bool:
    # write your code below
    raise NotImplementedError
    # write your code above

  def delete(self, k: int) -> bool:
    # write your code below
    raise NotImplementedError
    # write your code above

  def inorder(self) -> List[int]:
    # write your code below
    raise NotImplementedError
    # write your code above

  def preorder(self) -> List[int]:
    # write your code below
    raise NotImplementedError
    # write your code above

  def postorder(self) -> List[int]:
    # write your code below
    raise NotImplementedError
    # write your code above

  def min(self) -> Optional[int]:
    # write your code below
    raise NotImplementedError
    # write your code above

  def max(self) -> Optional[int]:
    # write your code below
    raise NotImplementedError
    # write your code above

  def height(self) -> int:
    # write your code below
    raise NotImplementedError
    # write your code above


if __name__ == "__main__":
  # Tu viet main theo yeu cau I/O ben tren.
  # write your code below
  # write your code above

