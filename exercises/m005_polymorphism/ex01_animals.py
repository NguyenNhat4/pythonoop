"""
Bài tập: Đa hình qua method chung (mức khá)
- Base Animal với method sound() -> str (raise NotImplementedError)
- Dog, Cat, Duck override sound()
- Hàm make_sounds(animals) -> list[str] gọi sound() đa hình
"""
from typing import List


class Animal:
    def sound(self) -> str:
        pass


class Dog(Animal):
    def sound(self) -> str:
        print("Woof")


class Cat(Animal):
    def sound(self) -> str:
        print("Meow")


class Duck(Animal):
    def sound(self) -> str:
        print("quack")

tmp_list = [Cat(),Dog(),Duck(),Dog(),Duck()]
def make_sounds(animals: List[Animal]) -> List[str]:
    """Gọi sound() cho từng animal và trả về list kết quả."""
    for animal in animals:
        animal.sound()
make_sounds(tmp_list)
    
a = Animal()
    
