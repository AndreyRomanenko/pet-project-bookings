from fastapi import APIRouter
from sqlalchemy import select

from app.database import async_session_maker
from app.hotels.models import Hotels
from app.hotels.dao import HotelDAO
from app.hotels.schemas import SHotel

router = APIRouter(
    prefix='/hotels',
    tags=["Отели"],

)

#

@router.get("")
async def get_booking():
    result = await HotelDAO.find_all()
    return result
