"""
Bài tập: Kế thừa cơ bản (mức khá)
- Base class Shape với phương thức area() -> float (raise NotImplementedError)
- Subclass: Rectangle(w, h), Circle(r)
- Tập trung vào override method và sử dụng super() nếu cần
"""
import math


class Shape:
    def area(self) -> float:
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        # TODO: gán thuộc tính, validate > 0
        raise NotImplementedError

    def area(self) -> float:
        # TODO: w * h
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        # TODO: gán thuộc tính, validate > 0
        raise NotImplementedError

    def area(self) -> float:
        # TODO: math.pi * r * r
        raise NotImplementedError
