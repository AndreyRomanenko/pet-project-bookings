from app.database import async_session_maker
from sqlalchemy import select, insert

from sqlalchemy.exc import SQLAlchemyError


# from app.logger import logger

class BaseDAO:
    model = None

    @classmethod
    async def find_by_id(cls, model_id):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().all()

    # @classmethod
    # async def add(cls, **data):
    #     async with async_session_maker() as session:
    #         query = insert(cls.model).values(**data)
    #         result = await session.execute(query)
    #         await session.commit()
    #         return result.mappings().first()

    @classmethod
    async def add(cls, **data):
        # try:
        query = insert(cls.model).values(**data).returning(cls.model.id)
        async with async_session_maker() as session:
            result = await session.execute(query)
            await session.commit()
            return result.mappings().first()
    # except (SQLAlchemyError, Exception) as e:
    #     if isinstance(e, SQLAlchemyError):
    #         msg = "Database Exc: Cannot insert data into table"
    #     elif isinstance(e, Exception):
    #         msg = "Unknown Exc: Cannot insert data into table"
    #
    #     #logger.error(msg, extra={"table": cls.model.__tablename__}, exc_info=True)
    #     return None
