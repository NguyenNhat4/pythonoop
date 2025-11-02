"""
Bài 04 - Đơn hàng (Order) và dòng hàng (OrderItem)
Mục tiêu: Tổ chức object có quan hệ has-a; validation cơ bản.
Ngữ cảnh: Tạo đơn hàng từ giỏ hàng với số lượng cụ thể.

Yêu cầu triển khai lớp:
- Product(name, price) như bài 01
- OrderItem(product: Product, qty: int)
- Order với _items: list[OrderItem]
  + add_item(product, qty)
  + total() -> int
  + to_dict() -> dict (xuất đơn hàng)

Yêu cầu I/O (tự viết main):
- Input: nhiều dòng đến EOF, mỗi dòng:
  + "add name price qty" để thêm một dòng hàng (product inline)
  + "total" | "dump"
- Output:
  + Với "total": in tổng tiền
  + Với "dump": in dict đơn hàng
"""
from typing import Dict, List


class Product:
    def __init__(self, name: str, price: int) -> None:
        self._name = name
        self._price = price

    def to_dict(self) -> Dict[str, int | str]:
        return {"name": self._name, "price": self._price}


class OrderItem:
    def __init__(self, product: Product, qty: int) -> None:
        # write your code below
        if qty <=0:
            raise ValueError("Quantity must be positive")
        self.product = product
        self.qty = qty
        # write your code above

    def subtotal(self) -> int:
        # write your code below
        return self.product._price * self.qty
        # write your code above

    def to_dict(self) -> Dict[str, int | str]:
        # write your code below
        return {"name": self.product._name,"price": self.product._price, "qty": self.qty, "subtotal": self.subtotal()}
        # write your code above


class Order:
    def __init__(self) -> None:
        # write your code below
        self.list_items: List[OrderItem] = []
        # write your code above

    def add_item(self, product: Product, qty: int) -> None:
        # write your code below
        if qty <= 0:
            return None
        for item in self.list_items:
            if item.product._name == product._name:
                item.qty += qty
                return
        self.list_items.append(OrderItem(product,qty))
        # write your code above

    def total(self) -> int:
        # write your code below
        return sum([i.subtotal() for i in self.list_items])
        # write your code above

    # def to_dict(self) -> Dict[str, List[Dict[str, int | str]]]:
        # write your code below
        
        # write your code above


if __name__ == "__main__":
    # Tự viết main theo yêu cầu I/O bên trên.
    # Gợi ý:
    # - Tạo Order; parse lệnh add/total/dump
    # write your code below
    # write your code above
    order = Order()
    with open(r"./orderitems.txt","r") as f:
        list = f.readlines()
        for j in list[1:]:
                value = [0,"",0,0]
                for i in j.split(" "):
                    i = i.replace("\n","")
                 
                    if i != '':
                        if value[0] == 1:
                            value[1] = i.strip()
                        elif value[0] == 2:
                            value[2] = int(i)
                        elif value[0] == 3:
                            value[3] = int(i)
                            p = Product(value[1],value[2])
                            order.add_item(p,value[3])
                            value = [0,"",0,0]
                        value[0]+=1
                        
                    
            # print(i[2])
            # name = i[1]
            # print(i[3])
            # quantity = i[3]
            # print("Current price is: ", price)
            # p = Product( name, int(price))
            # order.add_item(p, quantity)
        
        print(order.total())
        # print(list[1].split(" ")[1])