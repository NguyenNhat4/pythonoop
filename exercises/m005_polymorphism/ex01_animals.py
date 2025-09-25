"""
Bài tập: Đa hình qua method chung (mức khá)
- Base Animal với method sound() -> str (raise NotImplementedError)
- Dog, Cat, Duck override sound()
- Hàm make_sounds(animals) -> list[str] gọi sound() đa hình
"""
from typing import List


class Animal:
    def sound(self) -> str:
        raise NotImplementedError


class Dog(Animal):
    def sound(self) -> str:
        raise NotImplementedError


class Cat(Animal):
    def sound(self) -> str:
        raise NotImplementedError


class Duck(Animal):
    def sound(self) -> str:
        raise NotImplementedError


def make_sounds(animals: List[Animal]) -> List[str]:
    """Gọi sound() cho từng animal và trả về list kết quả."""
    raise NotImplementedError
