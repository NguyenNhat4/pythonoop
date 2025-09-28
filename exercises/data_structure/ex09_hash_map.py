"""
Bai 09 (kha) - Bang bam (HashMap) voi bucket chaining
Muc tieu: Hieu ve bam, dung bucket (list) de xu ly va resize theo load factor.
Ngu canh: Tu xay dung Map co put/get/delete.

Yeu cau trien khai lop:
- class HashMap(initial_capacity: int = 8, load_factor: float = 0.75)
  + set(key: object, value: object) -> None
  + get(key: object) -> object | None
  + delete(key: object) -> bool
  + contains(key: object) -> bool
  + keys() -> list[object]
  + values() -> list[object]
  + size() -> int
  + (goi y) _resize(new_capacity: int) -> None

Yeu cau I/O (tu viet main):
- Input: "set k v" | "get k" | "del k" | "has k" | "keys" | "values" | "size"
"""
from typing import List, Optional, Tuple


class HashMap:
  def __init__(self, initial_capacity: int = 8, load_factor: float = 0.75) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above

  def set(self, key: object, value: object) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above

  def get(self, key: object) -> Optional[object]:
    # write your code below
    raise NotImplementedError
    # write your code above

  def delete(self, key: object) -> bool:
    # write your code below
    raise NotImplementedError
    # write your code above

  def contains(self, key: object) -> bool:
    # write your code below
    raise NotImplementedError
    # write your code above

  def keys(self) -> List[object]:
    # write your code below
    raise NotImplementedError
    # write your code above

  def values(self) -> List[object]:
    # write your code below
    raise NotImplementedError
    # write your code above

  def size(self) -> int:
    # write your code below
    raise NotImplementedError
    # write your code above

  def _resize(self, new_capacity: int) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above


if __name__ == "__main__":
  # Tu viet main theo yeu cau I/O ben tren.
  # write your code below
  # write your code above

