"""
Bài tập: Encapsulation với tài khoản ngân hàng (mức khá)
- Class BankAccount với thuộc tính private: _owner, _balance
- deposit(amount), withdraw(amount), balance (property read-only)
- Yêu cầu: validate dữ liệu, không âm, không lộ balance trực tiếp qua biến public
"""
from typing import Final


class BankAccount:
    def __init__(self, owner: str, initial_balance: int = 0) -> None:
        # TODO: validate owner, initial_balance >= 0
        raise NotImplementedError

    def deposit(self, amount: int) -> None:
        # TODO: amount > 0
        raise NotImplementedError

    def withdraw(self, amount: int) -> None:
        # TODO: amount > 0 và không vượt quá số dư
        raise NotImplementedError

    @property
    def balance(self) -> int:
        # TODO: trả về số dư (read-only)
        raise NotImplementedError
