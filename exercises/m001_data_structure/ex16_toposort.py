"""
Bai 16 (kha) - Sap xep topo (Topological Sort) cho DAG
Muc tieu: Ap dung Kahn/DFS de toposort; phat hien chu trinh.
Ngu canh: Lam viec voi do thi co huong DAG.

Yeu cau trien khai lop:
- class DiGraph
  + add_edge(u: object, v: object) -> None
  + toposort_kahn() -> list[object] | None  (None neu co chu trinh)
  + toposort_dfs() -> list[object] | None  (None neu co chu trinh)
  + has_cycle() -> bool

Yeu cau I/O (tu viet main):
- Tu thiet ke lenh de them canh va in thu tu topo.
"""
from __future__ import annotations
from typing import Dict, List, Optional, Set


class DiGraph:
  def __init__(self) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above

  def add_edge(self, u: object, v: object) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above

  def toposort_kahn(self) -> Optional[List[object]]:
    # write your code below
    raise NotImplementedError
    # write your code above

  def toposort_dfs(self) -> Optional[List[object]]:
    # write your code below
    raise NotImplementedError
    # write your code above

  def has_cycle(self) -> bool:
    # write your code below
    raise NotImplementedError
    # write your code above


if __name__ == "__main__":
  # Tu viet main theo yeu cau I/O ben tren.
  # write your code below
  # write your code above

