from ex01 import Student
# ==================== TEST CASES ====================
print("=" * 50)
print("TEST 1: Tạo student và kiểm tra attributes")
print("=" * 50)

student1 = Student("Minh", 20, "CS001", "Computer Science")
assert student1.name == "Minh", "❌ Sai: name không đúng"
assert student1.age == 20, "❌ Sai: age không đúng"
assert student1.student_id == "CS001", "❌ Sai: student_id không đúng"
assert student1.major == "Computer Science", "❌ Sai: major không đúng"
print("✅ PASS: Attributes đúng!")

print("\n" + "=" * 50)
print("TEST 2: Method introduce()")
print("=" * 50)
print("Expected output:")
print("Hi, I'm Minh, 20 years old. Student ID: CS001, Major: Computer Science")
print("\nYour output:")
student1.introduce()

print("\n" + "=" * 50)
print("TEST 3: Method study()")
print("=" * 50)
print("Expected output:")
print("Minh is studying Computer Science")
print("\nYour output:")
student1.study()

print("\n" + "=" * 50)
print("TEST 4: Tạo nhiều students")
print("=" * 50)

student2 = Student("Lan", 19, "BUS002", "Business")
student3 = Student("Hùng", 21, "ENG003", "Engineering")

students = [student1, student2, student3]
for s in students:
    s.introduce()
    s.study()
    print()

print("✅ Nếu không có lỗi ở trên, bạn đã hoàn thành bài 1!")