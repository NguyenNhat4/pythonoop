print("=" * 50)
print("DEMO 5: PARSE DATA TỪ FILE")
print("=" * 50)

# Tạo file products.txt
print("\n[Bước 1] Tạo file 'products.txt'")
products_data = """iphone 20000000
samsung 15000000
laptop 25000000
tablet 10000000
headphone 5000000"""

with open('products.txt', 'w', encoding='utf-8') as f:
    f.write(products_data)

print("📄 Nội dung file 'products.txt':")
print(products_data)

# Đọc và parse
print("\n[Bước 2] Đọc và parse thành list of dict:")

products_list = []
with open('products.txt', 'r', encoding='utf-8') as f:
    for line in f:
        # Bỏ khoảng trắng đầu/cuối và tách theo space
        parts = line.strip().split()
        
        if len(parts) == 2:
            name = parts[0]
            price = int(parts[1])
            products_list.append({'name': name, 'price': price})

print("✅ Kết quả parse:")
for p in products_list:
    print(f"  - {p['name']}: {p['price']:,}đ")

# Tính toán
print(f"\n📊 Thống kê:")
print(f"  - Tổng số sản phẩm: {len(products_list)}")
print(f"  - Tổng giá trị: {sum(p['price'] for p in products_list):,}đ")
print(f"  - Sản phẩm rẻ nhất: {min(products_list, key=lambda x: x['price'])['name']}")
print(f"  - Sản phẩm đắt nhất: {max(products_list, key=lambda x: x['price'])['name']}")
print()