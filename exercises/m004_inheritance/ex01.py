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
    def __init__(self,name,age,student_id,major):
        super().__init__(name,age)
        self.student_id = student_id
        self.major = major

    def introduce(self):
        print(f"I am {self.name}, {self.age} years old", f"my student ID is : {self.student_id}, my major is {self.major}.")




a = Person("Huy",16)
b = Person("Trang",15)

a.introduce()
b.introduce()

c = Student("Lan",14,"A","student")
d = Student("Mai",17,"B","student")
c.introduce()
d.introduce()