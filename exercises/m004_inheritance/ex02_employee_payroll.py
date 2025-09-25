"""
Bài tập: Kế thừa và mở rộng hành vi (mức khá)
- Base class Employee(name)
- Subclass: FullTimeEmployee(name, monthly_salary), PartTimeEmployee(name, hourly_rate, hours)
- pay() -> int: trả về thu nhập, có thể override ở subclass
"""


class Employee:
    def __init__(self, name: str) -> None:
        # TODO: validate
        raise NotImplementedError

    def pay(self) -> int:
        # TODO: base có thể raise NotImplementedError
        raise NotImplementedError


class FullTimeEmployee(Employee):
    def __init__(self, name: str, monthly_salary: int) -> None:
        # TODO: super().__init__ và validate
        raise NotImplementedError

    def pay(self) -> int:
        # TODO: trả về monthly_salary
        raise NotImplementedError


class PartTimeEmployee(Employee):
    def __init__(self, name: str, hourly_rate: int, hours: int) -> None:
        # TODO: super().__init__ và validate
        raise NotImplementedError

    def pay(self) -> int:
        # TODO: hourly_rate * hours
        raise NotImplementedError
