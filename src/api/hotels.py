from fastapi import Query, APIRouter, Body
from src.schemas.hotels import Hotel, HotelPATCH
from src.api.dependencies import PaginationDep
from src.database import async_session_maker
from sqlalchemy import insert, select
from src.models.hotels import HotelsOrm
from repositories.hotels import HotelsRepository


router = APIRouter(prefix='/hotels', tags=['Отели'])


@router.get("")
async def  get_hotels(
        pagination: PaginationDep, 
        location: str | None = Query(None, description='Локация'), 
        title: str | None = Query(None, description='Название отеля'),
    ):
    per_page = pagination.per_page or 5
    async with async_session_maker() as session:
        return await HotelsRepository(session).get_all(
            location = location, 
            title = title, 
            limit = per_page, 
            offset = per_page * (pagination.page-1) 
        )

    
    

@router.post('')
async def create_hotel(hotel_data : Hotel = Body(openapi_examples={
    '1': {'summary': 'Сочи', 'value': {
        'title': 'Отель Сочи 5 звезд',
        'location': 'ул. Моря 1',
    }},
    '2': {'summary': 'Дубай', 'value': {
        'title': 'Отель Дубай 5 звезд',
        'location': 'ул. Шейха 2',
    }}
})
):
    async with async_session_maker() as session:
        hotel = await HotelsRepository(session).add(**hotel_data.model_dump())
        await session.commit()
    return {'status': 'OK', "data" : hotel}


@router.put('/{hotel_id}')
def change_hotel_put(hotel_id:int, hotel_data: Hotel):
    global hotels
    for hotel in hotels:
        if hotel['id'] == hotel_id:
            hotel['title'] = hotel_data.title
            hotel['name'] = hotel_data.name
    return {'status': 'OK'}


@router.patch('/{hotel_id}')
def change_hotel_patch(hotel_id:int, hotel_data: HotelPATCH ):
    global hotels
    for hotel in hotels:
        if hotel['id'] == hotel_id:
            if hotel_data.title:
                hotel['title'] = hotel_data.title
            if hotel_data.name:
                hotel['name'] = hotel_data.name
    return {'status': 'OK'}
        

@router.delete('/{hotel_id}')
def delete_hotel(hotel_id : int):
    global hotels
    hotels = [hotel for hotel in hotels if hotel['id'] != hotel_id]
    return {'status': 'OK'}