from os import getenv

from jwt import decode, encode


def sign_token(user_data: dict) -> str:
    return encode(user_data, getenv("SECRET_SALT"), algorithm="HS256")


def verify_token(token: str) -> bool:
    return decode(token, getenv("SECRET_SALT"), algorithms=["HS256"])
