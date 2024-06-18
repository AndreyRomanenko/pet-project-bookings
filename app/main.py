import uvicorn
from fastapi import FastAPI, Query, Depends, requests

from typing import Optional
from datetime import date
from pydantic import BaseModel
from app.bookings.router import router as router_bookings
from app.hotels.router import router as router_hotels
from app.users.router import router as router_users

#
#
# app = FastAPI()
#
# @app.get("/hotels")
# async def root():
#     return {"Отель Бридж Резорт 5 звёзд"}
#
#
#
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


#
# async def task_1():
#     await asyncio.sleep(2)
#     print("Завершена первая задача")
#
# async def task_2():
#     await asyncio.sleep(1)
#     print("Завершена вторая задача")
#
# async def task_3():
#     await asyncio.sleep(0.01)
#     print("Я завершаюсь последней. Но почему?")
#
# async def main():
#     task1 = asyncio.create_task(task_1())
#     print(task1)
#     task2 = asyncio.create_task(task_2())
#     print(task2)
#     tasks = [task1, task2]
#     for task in tasks:
#         print(task)
#         await task
#
#     await task_3()
#
# asyncio.run(main())

app = FastAPI(
    title="Бронирование Отелей",
    #version="0.1.0",
    #root_path="/api",
)

app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_hotels)


# @app.get("/{location}")
# def get_hotels(
#         location: str,
#         date_from: date,
#         date_to: date,
#
# ) -> list[SchemaHotel]:
#     hotels = [<HotelsModel 1>, <HotelsModel 2>]
#     return hotels

class HotelsSearchArgs:
    def __init__(
        self,
        hotel_id: int,
        date_from: date,
        date_to: date,
        location: Optional[str] = None,
        stars: Optional[int] = Query(None, ge=1, le=5)
):
        self.hotel_id = hotel_id
        self.date_from = date_from
        self.date_to = date_to
        self.location = location
        self.stars = stars


class SchemaBookingPost(BaseModel):
    room_id: int
    date_from: date
    date_to: date
    price: int


class SHotel(BaseModel):
    address: str
    name: str
    stars: int


@app.get("/hotels_old")
def get_hotels(
     search_args: HotelsSearchArgs = Depends()
     ):

    hotels = [
        {
        "address": "Гагарина 1",
        "name": "Meeru",
        "stars": 5,
        },
    ]
    return search_args

### Было
@app.get("/diff_hotels")
def get_hotels(
        hotel_id: int,
        date_from: date,
        date_to: date,
        location: Optional[str] = None,
        stars: Optional[int] = Query(None, ge=1, le=5)
     ) -> list[SHotel]:

    hotels = [
        {
        "address": "Галушина 1",
        "name": "Meeru",
        "stars": 5,
        },
    ]
    return hotels

# @app.post("/bookings")
# def add_bookings(booking: SchemaBookingPost):
#     pass
#
#     r = requests.get(f"127.0.0.1:8000/hotels/{hotel_id}", params={"date_from":"today", "date_to":"tomorrow"})


# if __name__ == "__main__":
#     uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)

# if __name__ == "__main__":
#     import uvicorn
#
#     import os.path
#     import sys
#     sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
#     uvicorn.run(
#         app="app.main:app",
#         reload=True,
#     )

if __name__ == "__main__":
    # run app on ther host and port
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000)