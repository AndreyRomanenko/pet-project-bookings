from fastapi import APIRouter
from sqlalchemy import select

from app.database import async_session_maker
from app.bookings.models import Bookings
from app.bookings.dao import BookingDAO
from app.bookings.dao import BookingDAO2
from app.bookings.schemas import SBooking

router = APIRouter(
    prefix='/bookings',
    tags=["Бронирование"],

)

#

@router.get("")
async def get_bookings():
    async with async_session_maker() as session:
        query = select(Bookings)  # IMPORT QUERY LIKE SELECT * FROM bookings;
        result = await session.execute(query)
        #print(result.all())

        return result.mappings().all()

@router.get("/test")
async def get_bookings_test():
    result = await BookingDAO2.find_all()
    return result

@router.get("test2")
async def get_booking_test2():
    result = await BookingDAO.find_all()
    return result



#
# @router.get("")
# # Переписан в отдельный dao file
# # async def get_bookings():
# #     async with async_session_maker() as session:
# #         query = select(Bookings)  # IMPORT QUERY LIKE SELECT * FROM bookings;
# #         result = await session.execute(query)
# #         return result.mappings().all()
# async def get_bookings() -> list[dict[str, SBooking]]:
#     result = await BookingDAO.find_all()
#     return result
#
#
#
#
#
# @router.get("/{bookings_id}")
# # async def get_bookings(booking_id):
# #     pass
#
# async def get_booking_id(bookings_id):
#     bookings_id = int(bookings_id)
#     result = await BookingDAO.find_one_or_none(bookings_id)
#     return result
