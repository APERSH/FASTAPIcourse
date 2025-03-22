from repositories.base import BaseRepository
from src.models.hotels import HotelsOrm
from sqlalchemy import select

class HotelsRepository(BaseRepository):
    model = HotelsOrm

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
        return result.scalars().all()
        