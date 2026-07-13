import re

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def is_valid_email(email: str) -> bool:
    return bool(email) and bool(EMAIL_REGEX.match(email))


def is_valid_username(username: str) -> bool:
    return bool(username) and len(username) >= 3 and username.isalnum()


def is_valid_password(password: str) -> bool:
    return bool(password) and len(password) >= 6
