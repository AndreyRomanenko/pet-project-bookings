from fastapi import APIRouter, HTTPException
from app.users.auth import get_password_hash
from app.users.schemas import SUserAuth
from app.users.dao import UserDAO

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"],

)

@router.get("/users")
#async def get_users() -> list[dict[str, SUserAuth]]:
async def get_users():
    result = await UserDAO.find_all()
    print(result)
    return result

@router.post("/register")
async def register_user(user_data: SUserAuth):
    print(f'user_date {user_data}')
    existing_user = await UserDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=500)
    hashed_password = get_password_hash(user_data.password)
    #hash_pass = hash_password(user_data.password)
    await UserDAO.add(email=user_data.email, hashed_password=hashed_password)


