from passlib.context import CryptContext
import bcrypt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# def hash_password(password):
#     pwd_bytes = password.encode('utf-8')
#     salt = bcrypt.gensalt()
#     hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
#     return hashed_password

# def verify_password(plain_password, hashed_password) -> bool:
#     return pwd_context.verify(plain_password, hashed_password)

