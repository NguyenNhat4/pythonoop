

class Product:
    def __init__(self, name: str, price: int, quantity: int) -> None:
 
        self._name = name  
        self._price = price
        self._quantity = quantity or 1
    def __repr__(self):
        return f"{self._name}: {self._price}: {self._quantity}"
    



def swap(list: list[Product], i, j):
    a = list[i]
    list[i] = list[j]
    list[j] = a



# def clone_sorted(l: list[Product],key: callable):
#     for i in range(len(l)-1):
#         maxindex = -1
#         maxvalue = 'a'
#         if isinstance(key(l[0]),int):
#             maxvalue = -9999
            
#         for j in range(len(l)-i):
#             print( key(l[j]),maxvalue)
            
#             if maxvalue < key(l[j]):
#                 maxindex = j
#                 maxvalue = key(l[j])
#         swap(l,maxindex,len(l)-1-i)
        




products = [
    Product("apple", 3000,200),
    Product("banana", 2000,300),
    Product("cherry", 1000,400),
    Product("date", 1000, 10),
    Product("elderberry", 1000, 10),
    Product("fig", 1000, 10),
    Product("grape", 1000, 10),
    Product("honeydew", 1000, 10),
    Product("kiwi", 1000, 10),
]


products_sort = sorted(products,key=lambda x: x._name)

print(products_sort)