print("=" * 50)
print("DEMO 2: GHI THÊM VỚI MODE 'a' (APPEND)")
print("=" * 50)

# Bước 1: Tạo file ban đầu
print("\n[Bước 1] Tạo file 'demo2.txt' với dữ liệu ban đầu")
with open('demo2.txt', 'w', encoding='utf-8') as f:
    f.write("Sản phẩm 1: iPhone - 20,000,000đ\n")
    f.write("Sản phẩm 2: Samsung - 15,000,000đ\n")

print("✅ File ban đầu:")
with open('demo2.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# Bước 2: Thêm sản phẩm mới (KHÔNG xóa data cũ)
print("\n[Bước 2] THÊM sản phẩm mới với mode 'a'")
input("Nhấn Enter để thêm sản phẩm...")

with open('demo2.txt', 'a', encoding='utf-8') as f:
    f.write("Sản phẩm 3: Laptop - 25,000,000đ\n")
    f.write("Sản phẩm 4: Tablet - 10,000,000đ\n")

print("✅ Đã thêm!")
print("\n📄 Nội dung file 'demo2.txt' SAU KHI THÊM:")
with open('demo2.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)

print("✅ Data cũ VẪN CÒN, data mới được THÊM VÀO CUỐI!\n")