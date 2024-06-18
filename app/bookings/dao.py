from app.database import async_session_maker
from app.bookings.models import Bookings
from sqlalchemy import select
from app.dao.base import BaseDAO


class BookingDAO(BaseDAO):
    model = Bookings

class BookingDAO2:

    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(Bookings)  # IMPORT QUERY LIKE SELECT * FROM bookings;
            result = await session.execute(query)
            return result.mappings().all()
