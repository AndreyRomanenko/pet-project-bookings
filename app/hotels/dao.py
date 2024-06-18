from datetime import date

from sqlalchemy import and_, func, or_, select

from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.database import async_session_maker, engine
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms
#from app.logger import logger


class HotelDAO(BaseDAO):
    model = Hotels

