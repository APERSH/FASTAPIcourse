from repositories.utils import rooms_ids_for_bookings
from src.models.bookings import BookingsOrm
from repositories.base import BaseRepository
from src.models.rooms import RoomsOrm
from src.schemas.rooms import Room, RoomWithRels
from sqlalchemy import select, func
from sqlalchemy.orm import selectinload, joinedload

class RoomsRepository(BaseRepository):
    model = RoomsOrm
    schema = Room
    async def get_filtered_by_time(
             self,
             hotel_id,
             date_from,
             date_to,
    ):

        rooms_ids_to_get = rooms_ids_for_bookings(date_from, date_to, hotel_id)

        query = (
            select(self.model)
            .options(joinedload(self.model.facilities))
            .filter(RoomsOrm.id.in_(rooms_ids_to_get))
        )

        result = await self.session.execute(query)
        return [RoomWithRels.model_validate(model) for model in result.unique().scalars().all()]
    
    async def get_one_or_none_with_rels(self, **filter_by):
        query = (
            select(self.model)
            .options(selectinload(self.model.facilities))
            .filter_by(**filter_by)
        )
        result = await self.session.execute(query)
        model = result.scalars().one_or_none()
        if model is None:
            return None
        return RoomWithRels.model_validate(model)