"""
Bai 14 (kha) - Trie (Prefix Tree)
Muc tieu: Quan ly ky tu theo cap, tim kiem theo prefix.
Ngu canh: Xay dung trie de luu tu dien don gian.

Yeu cau trien khai lop:
- class TrieNode
  + children: dict[str, TrieNode]
  + is_end: bool
- class Trie
  + insert(word: str) -> None
  + search(word: str) -> bool
  + starts_with(prefix: str) -> bool
  + (nang cao) delete(word: str) -> bool
  + (nang cao) suggest(prefix: str, k: int | None = None) -> list[str]

Yeu cau I/O (tu viet main):
- Input: "ins w" | "has w" | "pre p" | (tuy chon) "del w" | "sg p [k]"
"""
from __future__ import annotations
from typing import Dict, List, Optional


class TrieNode:
  def __init__(self) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above


class Trie:
  def __init__(self) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above

  def insert(self, word: str) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above

  def search(self, word: str) -> bool:
    # write your code below
    raise NotImplementedError
    # write your code above

  def starts_with(self, prefix: str) -> bool:
    # write your code below
    raise NotImplementedError
    # write your code above

  def delete(self, word: str) -> bool:
    # (nang cao) write your code below
    raise NotImplementedError
    # write your code above

  def suggest(self, prefix: str, k: Optional[int] = None) -> List[str]:
    # (nang cao) write your code below
    raise NotImplementedError
    # write your code above


if __name__ == "__main__":
  # Tu viet main theo yeu cau I/O ben tren.
  # write your code below
  # write your code above

