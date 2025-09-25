"""
Bài tập: ABC và interface-like (mức khá-nâng cao)
- Dùng abc.ABC và @abstractmethod cho Shape3D với volume()
- Subclass: Cube(edge), Sphere(radius)
- Hàm total_volume(shapes) -> float
"""
import abc
import math
from typing import List


class Shape3D(abc.ABC):
    @abc.abstractmethod
    def volume(self) -> float:  # pragma: no cover
        raise NotImplementedError


class Cube(Shape3D):
    def __init__(self, edge: float) -> None:
        # TODO: validate
        raise NotImplementedError

    def volume(self) -> float:
        # TODO: edge ** 3
        raise NotImplementedError


class Sphere(Shape3D):
    def __init__(self, radius: float) -> None:
        # TODO: validate
        raise NotImplementedError

    def volume(self) -> float:
        # TODO: 4/3 * pi * r^3
        raise NotImplementedError


def total_volume(shapes: List[Shape3D]) -> float:
    raise NotImplementedError
