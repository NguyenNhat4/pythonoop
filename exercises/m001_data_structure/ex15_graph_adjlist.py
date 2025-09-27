"""
Bai 15 (kha) - Do thi (Graph) bang danh sach ke
Muc tieu: Quan ly dinh/canh, BFS/DFS, duong di ngan nhat tren do thi vo huong khong trong so.
Ngu canh: Xay dung Graph co ban, vo huong hoac co huong.

Yeu cau trien khai lop:
- class Graph(directed: bool = False)
  + add_vertex(v: object) -> None
  + add_edge(u: object, v: object) -> None
  + neighbors(u: object) -> list[object]
  + bfs(start: object) -> list[object]
  + dfs(start: object) -> list[object]
  + shortest_path_unweighted(s: object, t: object) -> list[object] | None

Yeu cau I/O (tu viet main):
- Tu thiet ke bo lenh de them dinh/canh va truy van BFS/DFS/path.
"""
from __future__ import annotations
from typing import Dict, List, Optional, Set


class Graph:
  def __init__(self, directed: bool = False) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above

  def add_vertex(self, v: object) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above

  def add_edge(self, u: object, v: object) -> None:
    # write your code below
    raise NotImplementedError
    # write your code above

  def neighbors(self, u: object) -> List[object]:
    # write your code below
    raise NotImplementedError
    # write your code above

  def bfs(self, start: object) -> List[object]:
    # write your code below
    raise NotImplementedError
    # write your code above

  def dfs(self, start: object) -> List[object]:
    # write your code below
    raise NotImplementedError
    # write your code above

  def shortest_path_unweighted(self, s: object, t: object) -> Optional[List[object]]:
    # write your code below
    raise NotImplementedError
    # write your code above


if __name__ == "__main__":
  # Tu viet main theo yeu cau I/O ben tren.
  # write your code below
  # write your code above

