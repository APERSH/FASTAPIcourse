from repositories.base import BaseRepository
from schemas.hotels import Hotel
from src.models.hotels import HotelsOrm
from sqlalchemy import select

class HotelsRepository(BaseRepository):
    model = HotelsOrm
    schema = Hotel

    async def get_all(self, location, title, limit, offset):
        query = select(HotelsOrm)
        if location:
            query = query.filter(HotelsOrm.location.icontains(location))
        if title:
            query = query.filter(HotelsOrm.title.icontains(title))
        query = (query        
            .limit(limit)
            .offset(offset)
        )
        result = await self.session.execute((query))
        return [Hotel.model_validate(hotel, from_attributes=True) for hotel in result.scalars().all()]
        