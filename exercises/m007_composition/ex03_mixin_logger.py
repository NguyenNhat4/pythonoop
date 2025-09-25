"""
Bài tập: Mixin cơ bản (mức nâng cao)
- Tạo mixin Loggable với method log(msg) -> str
- Class ServiceA, ServiceB kế thừa mixin và class cơ sở chung BaseService
- Kiểm tra đa kế thừa và dùng super() nếu cần
"""


class Loggable:
    def log(self, message: str) -> str:
        # TODO: trả về chuỗi log đơn giản: f"[LOG] {message}"
        raise NotImplementedError


class BaseService:
    def __init__(self, name: str) -> None:
        # TODO: validate name
        raise NotImplementedError


class ServiceA(Loggable, BaseService):
    def process(self) -> str:
        # TODO: trả về chuỗi dùng self.log
        raise NotImplementedError


class ServiceB(Loggable, BaseService):
    def process(self) -> str:
        # TODO
        raise NotImplementedError
