print("=" * 50)
print("DEMO 4: CÁC CÁCH ĐỌC FILE")
print("=" * 50)

# Tạo file mẫu
with open('demo4.txt', 'w', encoding='utf-8') as f:
    f.write("Dòng 1\nDòng 2\nDòng 3\nDòng 4\nDòng 5\n")

# Cách 1: read() - đọc toàn bộ thành string
print("\n[Cách 1] Dùng read() - đọc toàn bộ file:")
with open('demo4.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(f"Type: {type(content)}")
    print(f"Content:\n{content}")

# Cách 2: readlines() - đọc thành list
print("\n[Cách 2] Dùng readlines() - đọc thành list:")
with open('demo4.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(f"Type: {type(lines)}")
    print(f"Content: {lines}")
    print(f"Số dòng: {len(lines)}")

# Cách 3: Loop - đọc từng dòng (tiết kiệm RAM)
print("\n[Cách 3] Loop từng dòng - tốt nhất cho file lớn:")
with open('demo4.txt', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        print(f"  Dòng {i}: {line.strip()}")  # strip() bỏ \n

print()