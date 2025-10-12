# Code không có inheritance - lặp lại nhiều các đối tượng có cùng thuộc tính phương thức giống nhau 
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def action(self):
        print(f"{self.name} is barking")
    
    def sound(self):
        print("Woof!")

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def action(self):
        print(f"{self.name} is spleeping")
    
    def sound(self):
        print("Meow!")
        

class Duck:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def action(self):
        print(f"{self.name} is swimming")
    
    def sound(self):
        print("Quack!")