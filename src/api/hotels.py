from fastapi import Query, APIRouter, Body
from src.schemas.hotels import Hotel, HotelPATCH, HotelAdd
from src.api.dependencies import PaginationDep
from src.database import async_session_maker
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


@router.get("/{hotel_id}")
async def get_hotel(hotel_id: int):
    async with async_session_maker() as session:
        return await HotelsRepository(session).get_one_or_none(id = hotel_id)
    
@router.post('')
async def create_hotel(hotel_data : HotelAdd = Body(openapi_examples={
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
        hotel = await HotelsRepository(session).add(hotel_data)
        await session.commit()
    return {'status': 'OK', "data" : hotel}


@router.put('/{hotel_id}')
async def change_hotel_put(hotel_id:int, hotel_data: HotelAdd):
    async with async_session_maker() as session:
        await HotelsRepository(session).edit(hotel_data, id = hotel_id)
        await session.commit()
    return {'status': 'OK'}


@router.patch('/{hotel_id}')
async def change_hotel_patch(hotel_id:int, hotel_data: HotelPATCH ):
    async with async_session_maker() as session:
        await HotelsRepository(session).edit(hotel_data, exclude_unset = True, id = hotel_id)
        await session.commit()
    return {'status': 'OK'}
        

@router.delete('/{hotel_id}')
async def delete_hotel(hotel_id : int):
    async with async_session_maker() as session:
        await HotelsRepository(session).delete(id = hotel_id)
        await session.commit()
    return {'status': 'OK'}