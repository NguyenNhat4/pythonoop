"""
Bài tập: Polymorphism theo chiến lược thanh toán (mức khá-nâng cao)
- Base PaymentMethod với pay(amount) -> str
- Subclass: Cash, CreditCard(masked_number), EWallet(provider)
- Hàm checkout(amount, method: PaymentMethod) -> str
"""


class PaymentMethod:
    def pay(self, amount: int) -> str:
        raise NotImplementedError


class Cash(PaymentMethod):
    def pay(self, amount: int) -> str:
        raise NotImplementedError


class CreditCard(PaymentMethod):
    def __init__(self, masked_number: str) -> None:
        # TODO: validate dạng "****-****-****-1234"
        raise NotImplementedError

    def pay(self, amount: int) -> str:
        raise NotImplementedError


class EWallet(PaymentMethod):
    def __init__(self, provider: str) -> None:
        # TODO: validate provider không rỗng
        raise NotImplementedError

    def pay(self, amount: int) -> str:
        raise NotImplementedError


def checkout(amount: int, method: PaymentMethod) -> str:
    raise NotImplementedError
