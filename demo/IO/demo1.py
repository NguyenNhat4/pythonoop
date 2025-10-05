print("=" * 50)
print("DEMO 1: GHI FILE VỚI MODE 'w' (WRITE - GHI ĐÈ)")
print("=" * 50)

# Bước 1: Tạo file mới
print("\n[Bước 1] Tạo file mới 'demo1.txt' với mode 'w'")
with open('demo1.txt', 'w', encoding='utf-8') as f:
    f.write("Dòng 1: Xin chào\n")
    f.write("Dòng 2: Python I/O\n")
    f.write("Dòng 3: File handling\n")

print("✅ Đã tạo file!")
print("\n📄 Nội dung file 'demo1.txt':")
with open('demo1.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# Bước 2: Ghi đè file (XÓA data cũ)
print("\n[Bước 2] Ghi ĐÈ file cũ với mode 'w' - DATA CŨ SẼ MẤT!")
input("Nhấn Enter để tiếp tục...")

with open('demo1.txt', 'w', encoding='utf-8') as f:
    f.write("Dòng MỚI: Data cũ đã bị xóa!\n")

print("⚠️  Đã ghi đè!")
print("\n📄 Nội dung file 'demo1.txt' BÂY GIỜ:")
with open('demo1.txt', 'r', encoding='utf-8') as f:
    print(f.read())

print("❌ Data cũ (Dòng 1, 2, 3) đã BÃ MẤT!\n")