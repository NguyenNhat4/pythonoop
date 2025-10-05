print("=" * 50)
print("DEMO 3: SO SÁNH 'w' vs 'a'")
print("=" * 50)

# Chuẩn bị 2 file giống nhau
print("\n[Chuẩn bị] Tạo 2 file giống nhau")
initial_content = "A\nB\nC\n"

with open('file_w.txt', 'w', encoding='utf-8') as f:
    f.write(initial_content)

with open('file_a.txt', 'w', encoding='utf-8') as f:
    f.write(initial_content)

print("📄 Nội dung ban đầu của CẢ 2 file:")
print(initial_content)

# Test mode 'w'
print("\n[Test 1] Ghi thêm vào file_w.txt với mode 'w':")
with open('file_w.txt', 'w', encoding='utf-8') as f:
    f.write("D\n")

print("📄 Kết quả file_w.txt:")
with open('file_w.txt', 'r', encoding='utf-8') as f:
    print(f.read())
print("❌ Chỉ còn 'D' - đã MẤT A, B, C!")

# Test mode 'a'
print("\n[Test 2] Ghi thêm vào file_a.txt với mode 'a':")
with open('file_a.txt', 'a', encoding='utf-8') as f:
    f.write("D\n")

print("📄 Kết quả file_a.txt:")
with open('file_a.txt', 'r', encoding='utf-8') as f:
    print(f.read())
print("✅ Có A, B, C, D - đã THÊM D vào cuối!\n")