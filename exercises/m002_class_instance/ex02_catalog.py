from typing import Dict, Optional, List
import math
from crud import get_product, create_product, init_schema ,Product,get_list_products,delete_product
# class Product:
#     def __init__(self, name: str, price: int) -> None:
#         try:
#             price = int(price)
#         except:
#             raise ValueError("Price must be an integer")
#         if price <= 0:
#             raise ValueError("Price must be greater than 0")
        
#         self._name = name.lower()
#         self._price = price

#     def to_dict(self) -> Dict[str, int | str]:
#         return {"name": self._name, "price": int(self._price)}

#     def copy(self) -> 'Product':
#         return Product(self._name, self._price)
    
#     def __repr__(self):
#         return f"Product(name={self._name}, price={self._price})"



class Catalog:
    def __init__(self) -> None:
        # write your code below
        # write your code above
        self.__items : Dict[str, Product] = {}
    def printitems(self)-> Dict[str, Product]:
        print(self.__items)
        
    def swap(self,list: list[Product], i, j):
        a = list[i]
        list[i] = list[j]
        list[j] = a

    def sortbytype(self, type: str , sortedtype: str)-> List[Product]: 
        reverse = False if sortedtype == "asd" else True
        list_product = list(self.__items.values())
        if type == "price":
            list_product.sort(key=lambda x: x._price, reverse=reverse)
        elif type == "name":
            list_product = sorted(list_product,key=lambda x: x.name, reverse=reverse)
        return list_product
    

    def clone_sorted(self,l: list[Product],key: callable, reverse: bool = False):
        
        if not reverse:
            for i in range(len(l)-1):
                    maxindex = -1
                    maxvalue = 'a'
                    if isinstance(key(l[0]),int):
                        maxvalue = -99999999999999999
                        
                    for j in range(len(l)-i):
                        print( key(l[j]),maxvalue)
                        
                        if maxvalue < key(l[j]) :
                            maxindex = j
                            maxvalue = key(l[j])
                    self.swap(l,maxindex,len(l)-1-i)
        else:
            for i in range(len(l)-1):
                    minindex = len(l)
                    minvalue = 'z'
                    if isinstance(key(l[0]),int):
                        minvalue = 99999999999999999
                        
                    for j in range(len(l)-i):
                        print( key(l[j]),minvalue)
                        
                        if minvalue > key(l[j]) :
                            minindex = j
                            minvalue = key(l[j])
                    self.swap(l,minindex,len(l)-1-i)
                    

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
        return self.__items.get(name.lower())

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
    def remove(self, name: str) -> bool:
        """
        Xóa sản phẩm khỏi catalog
        Return True nếu xóa thành công
        Return False nếu sản phẩm không tồn tại
        """
        name = name.lower()
        product = self.__items.get(name, None)
        if product is None:
            return False
        
        
        self.__items.pop(name)
        return True

    def count(self) -> int:
        """Đếm tổng số sản phẩm trong catalog"""
        return len(self.__items)

    
    def get_all_names(self) -> List[str]:
        """
        Lấy danh sách tên tất cả sản phẩm
        Return: ['hair spray', 'iphone', 'samsung']
        """
        return list(self.__items.keys())
    
    def get_total_value(self) -> int:
        """
        Tính tổng giá trị tất cả sản phẩm trong catalog
        Ví dụ: có 3 sản phẩm giá 100, 200, 300 → return 600
        """
        product_list : List[Product] = list(self.__items.values())
        
        total_value = 0
        
        for product in product_list:
            total_value += product._price
        return total_value
   
    
    def get_cheapest(self) -> Optional[Product]:
        """
        Tìm sản phẩm rẻ nhất
        Gợi ý: dùng min() với key=lambda p: p._price
        """
        if not self.__items:
            return None
        return min(self.__items.values(), key=lambda p: p._price)   
    
    
    def get_most_expensive(self) -> Optional[Product]:
        """
        Tìm sản phẩm đắt nhất
        Gợi ý: dùng max() với key=lambda p: p._price
        """
        if not self.__items:
            return None
        return max(self.__items.values(), key=lambda p: p._price)



if __name__ == "__main__":
    # Tự viết main theo yêu cầu I/O bên trên.
    # Gợi ý:
    # - Tạo Catalog, đọc dòng lệnh tới EOF, parse và gọi phương thức
    # write your code below
    # write your code above
    # p1 = Product("Hair Spray",20000)
    # p2 = Product("Iphone", 600000)
    # p3 = Product("Samsung", 400000)
    # p4 = Product("a", 400000)
    # p4 = Product("b", 400000)
    
    # c = Catalog()
    # c.add(p1)
    # c.add(p2)
    # c.add(p3)
    # c.add(p4)
    # print(c.sortbytype("price","ded"))
    
    
    catalog = Catalog()
    init_schema()
    
    while True:
        lines = input().strip().split()
        print(lines)
        command = lines[0]
        # name = lines[1]
        # price = lines[2]
        if command == "add":
            # p = Product(name=lines[1],price=lines[2])
            create_product(name=lines[1],price=lines[2])
        if command == "dump":
            print(get_list_products())
            # catalog.add(p)
        if command == "delete":
            for i in lines[1:]:
                delete_product(int(i))
            
        # elif command == "search":   
        #     product_tmp: Product = catalog.search_by_name(lines[1])
        #     print(product_tmp.to_dict())
        # elif command == "dump":
        #     print(catalog.to_dict())
            
        # elif command == "filter":
        #     min_price = int(lines[1])
        #     max_price = int(lines[2])
        #     print(catalog.get_by_price_range(min_price, max_price))
 
        # if command == "sort":
        #     print(catalog.sortbytype(lines[1].strip(),lines[2].strip()))
            
         
            