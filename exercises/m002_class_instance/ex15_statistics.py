"""
Bài 15 - Thống kê bán hàng (Sales Statistics)
Mục tiêu: Luyện aggregations (sum, max, min, avg), sorting, grouping.
Ngữ cảnh: Phân tích dữ liệu bán hàng, tìm top products, tính revenue.

PYTHON FUNDAMENTALS PRACTICE:
1. Aggregations: sum(), max(), min(), len()
2. Sorting: sorted() với key parameter, reverse parameter
3. Grouping: defaultdict, dict với loops
4. Statistics: average, median, percentile
5. Advanced: max() với key, min() với key

Yêu cầu triển khai lớp:
- Class Product(name: str, price: int, category: str)
- Class Sale(product: Product, quantity: int, timestamp: str)
- Class SalesStats
  + __init__(sales: list[Sale])
  + total_revenue() -> int
  + top_products(n: int) -> list[tuple[str, int]]  # (name, revenue)
  + revenue_by_category() -> dict[str, int]
  + average_order_value() -> float
  + best_selling_product() -> Product
  + worst_selling_product() -> Product
  + sales_count_by_day() -> dict[str, int]

Yêu cầu I/O (tự viết main):
- Input: nhiều dòng đến EOF:
  + "sale product_name price category qty timestamp"
  + "revenue" - tổng doanh thu
  + "top n" - top n products
  + "by_category" - revenue theo category
  + "avg" - average order value
  + "best" - best selling product
  + "worst" - worst selling product
- Output: tùy command
"""
from typing import List, Tuple, Dict
from collections import defaultdict


class Product:
    def __init__(self, name: str, price: int, category: str) -> None:
        self._name = name
        self._price = price
        self._category = category

    def to_dict(self) -> Dict[str, int | str]:
        return {"name": self._name, "price": self._price, "category": self._category}


class Sale:
    def __init__(self, product: Product, quantity: int, timestamp: str) -> None:
        self._product = product
        self._quantity = quantity
        self._timestamp = timestamp

    def revenue(self) -> int:
        """Doanh thu của sale này"""
        return self._product._price * self._quantity

    def day(self) -> str:
        """Lấy ngày từ timestamp (YYYY-MM-DD)"""
        return self._timestamp.split()[0] if ' ' in self._timestamp else self._timestamp


class SalesStats:
    def __init__(self, sales: List[Sale]) -> None:
        # write your code below
        raise NotImplementedError
        # write your code above

    def total_revenue(self) -> int:
        """
        Tổng doanh thu
        Gợi ý: dùng sum() với generator expression
        sum(sale.revenue() for sale in self._sales)
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def top_products(self, n: int) -> List[Tuple[str, int]]:
        """
        Top n products theo doanh thu
        Gợi ý:
        1. Group sales by product name, tính tổng revenue
        2. Sort theo revenue (descending)
        3. Lấy n đầu tiên
        Return: [(product_name, total_revenue), ...]
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def revenue_by_category(self) -> Dict[str, int]:
        """
        Doanh thu theo category
        Gợi ý: dùng defaultdict(int) hoặc dict với setdefault
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def average_order_value(self) -> float:
        """
        Giá trị trung bình mỗi order
        Gợi ý: total_revenue / số lượng sales
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def best_selling_product(self) -> Product:
        """
        Sản phẩm bán chạy nhất (theo quantity)
        Gợi ý:
        1. Group by product, sum quantities
        2. Dùng max() với key parameter
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def worst_selling_product(self) -> Product:
        """
        Sản phẩm bán ít nhất (theo quantity)
        Gợi ý: tương tự best_selling nhưng dùng min()
        """
        # write your code below
        raise NotImplementedError
        # write your code above

    def sales_count_by_day(self) -> Dict[str, int]:
        """
        Số lượng sales theo ngày
        Gợi ý: group by sale.day()
        """
        # write your code below
        raise NotImplementedError
        # write your code above


if __name__ == "__main__":
    """
    MINI-EXERCISES - Python Fundamentals Practice

    Exercise 1: Aggregations
    - Tạo list prices = [15000, 20000, 25000, 30000, 10000]
    - Tính: sum(), max(), min(), len()
    - Tính average: sum(prices) / len(prices)
    - Tìm index của max: prices.index(max(prices))

    Exercise 2: Sorting basics
    - Sort ascending: sorted(prices)
    - Sort descending: sorted(prices, reverse=True)
    - Sort products by name: sorted(products, key=lambda p: p._name)
    - Sort by multiple keys: sorted(products, key=lambda p: (p._category, p._price))

    Exercise 3: Max/Min with key
    - Tìm product đắt nhất: max(products, key=lambda p: p._price)
    - Tìm product rẻ nhất: min(products, key=lambda p: p._price)
    - Tìm tên dài nhất: max(products, key=lambda p: len(p._name))

    Exercise 4: Grouping với defaultdict
    - from collections import defaultdict
    - groups = defaultdict(int)
    - for sale in sales:
    -     groups[sale._product._category] += sale.revenue()

    Exercise 5: Grouping với dict thường
    - groups = {}
    - for sale in sales:
    -     cat = sale._product._category
    -     groups[cat] = groups.get(cat, 0) + sale.revenue()

    Exercise 6: Advanced aggregations
    - Top 3 categories by revenue:
    -   sorted(groups.items(), key=lambda x: x[1], reverse=True)[:3]
    - Percentage của mỗi category:
    -   {cat: rev/total*100 for cat, rev in groups.items()}

    Exercise 7: Statistics calculations
    - Median: sorted_prices[len(sorted_prices)//2]
    - Range: max(prices) - min(prices)
    - Count items > threshold: sum(1 for p in prices if p > 20000)
    """
    # Tự viết main theo yêu cầu I/O bên trên.
    # Gợi ý:
    # - Parse input để tạo list[Sale]
    # - Tạo SalesStats(sales)
    # - Parse commands và gọi methods
    # write your code below
    # write your code above
