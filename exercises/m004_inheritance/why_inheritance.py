# Code không có inheritance - lặp lại nhiều
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def eat(self):
#         print(f"{self.name} is eating")
    
#     def bark(self):
#         print("Woof!")

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def eat(self):
#         print(f"{self.name} is eating")
    
#     def meow(self):
#         print("Meow!")
        
        
        
        ############################ Inheritance ############################
        
class Animal:  # Parent/Base class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f"{self.name} is eating")



class Dog(Animal):  # Child class
    def bark(self):
        print("Woof!")



class Cat(Animal):
    def __init__(self,name,age,id):
        super().__init__(name,age)
        self.id = id
    def print_id(self):
        print(self.id)
    def meow(self):
        print("Meow!")
        
class Duck(Animal):
    def quack(self):
        print("Quack!")
        
        
c = Cat("Kitty", 3, 123)
c.print_id()
d = Dog("Buddy", 5)
c.eat()
d.bark()
d.eat()





        ############################ thêm attributes? ############################
# class Animal:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#         print(f"Animal {name} created!")

# class Dog(Animal):
#     def __init__(self, name, age, breed):
#         # super().__init__(name, age)  # Gọi __init__ của chas
#         self._breed = breed

# buddy = Dog("Buddy", 3, "Golden Retriever")


# print(buddy._name)
# tại sao cần super()?

################### 

# class Vehicle:
#     pass

# class Car(Vehicle):
#     pass


