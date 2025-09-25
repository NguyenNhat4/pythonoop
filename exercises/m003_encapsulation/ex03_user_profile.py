"""
Bài tập: Ẩn dữ liệu nhạy cảm (mức khá)
- Class UserProfile với: username (public), _email (private), _password_hash (private)
- set_email(email), set_password(raw_password)
- verify_password(raw_password) -> bool
- Lưu ý: không trả về password hay hash ra ngoài; kiểm tra tối thiểu cho email hợp lệ (chỉ cần '@')
"""
import hashlib


class UserProfile:
    def __init__(self, username: str) -> None:
        # TODO: validate username không rỗng
        raise NotImplementedError

    def set_email(self, email: str) -> None:
        # TODO: check '@'
        raise NotImplementedError

    def set_password(self, raw_password: str) -> None:
        # TODO: hash SHA256 và lưu private
        raise NotImplementedError

    def verify_password(self, raw_password: str) -> bool:
        # TODO: so sánh hash
        raise NotImplementedError
