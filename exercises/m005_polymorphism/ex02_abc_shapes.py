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
        pass


class Cube(Shape3D):
    def __init__(self, edge: float) -> None:
        # TODO: validate
        self.edge = edge

    def volume(self) -> float:
        # TODO: edge ** 3
        return self.edge ** 3


class Sphere(Shape3D):
    def __init__(self, radius: float) -> None:
        # TODO: validate
        self.radius = radius

    def volume(self) -> float:
        # TODO: 4/3 * pi * r^3
        return (4//3)*(self.radius ** 3) * math.pi


# def total_volume(shapes: List[Shape3D]) -> float:
#     raise NotImplementedError

# a  =  Cube(5)
# print(a.volume())
list_tmp = [Cube(3),Sphere(4)]
total_volume = 0
for i in list_tmp:
    print(i.volume())
    total_volume += i.volume()

print(total_volume)