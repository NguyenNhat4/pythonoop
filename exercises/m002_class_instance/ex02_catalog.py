from typing import Dict, Optional, List


class Product:
    def __init__(self, name: str, price: int) -> None:
        # write your code below
        # write your code above
        
        self._name = name.lower()
        self._price = price

    def to_dict(self) -> Dict[str, int | str]:
        return {"name": self._name, "price": int(self._price)}


class Catalog:
    def __init__(self) -> None:
        # write your code below
        # write your code above
        self.__items : Dict[str, Product] = {}

    def add(self, product: Product) -> None:
        # write your code below
        # write your code above
        product_dict = product.to_dict()
        product_name = product_dict.get("name")
        product_price = product_dict.get("price")
        if product_name == '' or product_name is None:
            return None 
        if product_name in list(self.__items.keys()):
            return None
        try:
            product_price = int(product_price)
        except:
            return None
        if product_price <= 0:
            return None
        self.__items[product_name] = product
        

    def search_by_name(self, name: str) -> Optional[Product]:
        return self.__items.get(name.lower(), None)

    def get_by_price_range(self, min_price: int, max_price: int) -> List[Dict[str, int | str]]:
        product_list = []
        for name, product in self.__items.items():    
            product_dict= product.to_dict()
            current_price =  product_dict.get("price")       
            if  min_price  <= current_price <= max_price:
                product_list.append(product.to_dict())
        return product_list
        
    # def sort_by_price(self, ascending: bool = True):
    #     raise NotImplementedError
        
    def get(self, name: str) -> Optional[Product]:
        # write your code below
        # write your code above
        return self.items.get(name)

    def to_dict(self) -> Dict[str, Dict[str, int | str]]:
        # write your code below
        # write your code above
        # for i,j in self.__items.items():
        #     print(i,j.to_dict())
        pmd = {}
        for i,j in self.__items.items():
          pmd[i] = j.to_dict()
        return pmd  

    # def update_price(self, name: str, new_price: int) -> bool:
    # """
    # Cập nhật giá sản phẩm
    # Return True nếu thành công, False nếu:
    # - Sản phẩm không tồn tại
    # - Giá mới <= 0
    # """
    # def remove(self, name: str) -> bool:
    # """
    # Xóa sản phẩm khỏi catalog
    # Return True nếu xóa thành công
    # Return False nếu sản phẩm không tồn tại
    # """
    # def count(self) -> int:
    # """Đếm tổng số sản phẩm trong catalog"""
    # def get_all_names(self) -> List[str]:
    # """
    # Lấy danh sách tên tất cả sản phẩm
    # Return: ['hair spray', 'iphone', 'samsung']
    # """
    # def get_total_value(self) -> int:
    # """
    # Tính tổng giá trị tất cả sản phẩm trong catalog
    # Ví dụ: có 3 sản phẩm giá 100, 200, 300 → return 600
    # """
    # def get_cheapest(self) -> Optional[Product]:
    # """Tìm sản phẩm rẻ nhất"""
    # # Gợi ý: dùng min() với key
    
    # def get_most_expensive(self) -> Optional[Product]:
    # """Tìm sản phẩm đắt nhất"""
    # def sort_by_price(self, ascending: bool = True) -> List[Dict[str, int | str]]:
    # """Sắp xếp sản phẩm theo giá"""
    # def  sort_by(field: str, ascending: bool = True) -> List[Dict[str, int | str]]:



if __name__ == "__main__":
    # Tự viết main theo yêu cầu I/O bên trên.
    # Gợi ý:
    # - Tạo Catalog, đọc dòng lệnh tới EOF, parse và gọi phương thức
    # write your code below
    # write your code above
    # p1 = Product("Hair Spray",20000)
    # p2 = Product("Iphone", 600000)
    # p3 = Product("Samsung", 400000)
    # p4 = Product("", 400000)
    # p4 = Product("", 400000)
    
    # c = Catalog()
    # c.add(p1)
    # c.add(p2)
    # c.add(p3)
    # c.add(p4)
    # print(c.get_by_price_range(20000, 600000))
    # print(c.to_dict())
    # print (c.to_dict())

    catalog = Catalog()
    while True:
        lines = input().strip().split()
        print(lines)
        command = lines[0]
        # name = lines[1]
        # price = lines[2]
        if command == "add":
            p = Product(lines[1],lines[2])
            catalog.add(p)
        elif command == "search":   
            product_tmp: Product = catalog.search_by_name(lines[1])
            print(product_tmp.to_dict())
        elif command == "dump":
            print(catalog.to_dict())
            
        elif command == "filter":
            min_price = int(lines[1])
            max_price = int(lines[2])
            print(catalog.get_by_price_range(min_price, max_price))
 
