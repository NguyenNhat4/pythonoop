"""
BÀI TẬP: Xây dựng hệ thống Person và Student

CHO SẴN:
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old")

"""
YÊU CẦU:
1. Tạo class Student kế thừa từ Person
2. Thêm attributes: student_id (string), major (string)
3. Override method introduce() để in thêm student_id và major
4. Tạo method study() in ra "{name} is studying {major}"
"""

# VIẾT CODE CỦA BẠN Ở ĐÂY:
class Student(Person):
    pass  # TODO: Implement this

