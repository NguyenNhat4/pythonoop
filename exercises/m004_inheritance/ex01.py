


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old")

# Yêu cầu:
# 1. Tạo class Student kế thừa Person
# 2. Thêm attribute: student_id, major
# 3. Override method introduce() để thêm info về student_id và major
# 4. Test bằng cách tạo 2 student objects