class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):  # ← Override: cùng tên method
        print("Hello from Child")
        


p = Parent()
c = Child()
p.greet()
c.greet()  # Output: "Hello from Child" (không phải Parent)