from repositories.utils import rooms_ids_for_bookings
from src.models.bookings import BookingsOrm
from repositories.base import BaseRepository
from src.models.rooms import RoomsOrm
from src.schemas.rooms import Room
from sqlalchemy import select, func

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

        return await self.get_filtered(RoomsOrm.id.in_(rooms_ids_to_get))