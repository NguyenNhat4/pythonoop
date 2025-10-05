print("=" * 50)
print("DEMO 7: XỬ LÝ LỖI")
print("=" * 50)

# Lỗi 1: File không tồn tại
print("\n[Lỗi 1] Đọc file không tồn tại:")
try:
    with open('khong_ton_tai.txt', 'r', encoding='utf-8') as f:
        data = f.read()
except FileNotFoundError as e:
    print(f" Lỗi: {e}")
    print(" Giải pháp: Kiểm tra file tồn tại trước khi đọc")

# Lỗi 2: Không có quyền ghi
# print("\n[Lỗi 2] Ghi vào thư mục không có quyền:")
# try:
#     with open('/root/test.txt', 'w', encoding='utf-8') as f:
#         f.write("test")
# except PermissionError as e:
#     print(f" Lỗi: {e}")
#     print(" Giải pháp: Ghi vào thư mục có quyền (như thư mục hiện tại)")

# Lỗi 3: Parse sai format
print("\n[Lỗi 3] Parse data sai format:")
bad_data = "product1 abc\nproduct2 2000\n"  # 'abc' không phải số

with open('bad_data.txt', 'w', encoding='utf-8') as f:
    f.write(bad_data)

print("📄 File có data lỗi:")
print(bad_data)

print("\nĐọc và parse:")
with open('bad_data.txt', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        parts = line.strip().split()
        if len(parts) == 2:
            name = parts[0]
            try:
                price = int(parts[1])
                print(f"  ✅ Dòng {i}: {name} - {price}")
            except ValueError:
                print(f"  ❌ Dòng {i}: Giá '{parts[1]}' không hợp lệ - BỎ QUA")
