import random


def create_product_data(filename: str = "products.txt", num_products: int = 10000000):
    """
    Tạo file txt chứa danh sách sản phẩm

    Args:
        filename: Tên file txt cần tạo
        num_products: Số lượng sản phẩm (mặc định 10 triệu)
    """
    with open(filename, 'w', encoding='utf-8') as f:
        for i in range(1, num_products + 1):
            product_name = f"product{i}"
            price = random.randint(1, 1000000000)  # Random từ 1 đến 1 tỷ
            f.write(f"add {product_name} {price}\n")

            # In progress mỗi 1 triệu sản phẩm
            if i % 1000000 == 0:
                print(f"Đã tạo {i:,} sản phẩm...")

    print(f"Hoàn thành! Đã tạo {num_products:,} sản phẩm trong file {filename}")


if __name__ == "__main__":
    # Tạo 10 triệu sản phẩm
    create_product_data("products.txt", 10000000)
