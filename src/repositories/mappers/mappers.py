from src.schemas.facilities import Facilities, RoomFacilities
from src.models.facilities import FacilitiesOrm, RoomsFacilitiesOrm
from src.models.bookings import BookingsOrm
from src.models.rooms import RoomsOrm
from src.models.users import UsersOrm
from src.schemas.bookings import Booking
from src.schemas.rooms import Room
from src.schemas.users import User
from src.models.hotels import HotelsOrm
from src.repositories.mappers.base import DataMapper
from src.schemas.hotels import Hotel


class HotelDataMapper(DataMapper):
    db_model = HotelsOrm
    schema = Hotel

class RoomDataMapper(DataMapper):
    db_model = RoomsOrm
    schema = Room

class UserDataMapper(DataMapper):
    db_model = UsersOrm
    schema = User

class BookingDataMapper(DataMapper):
    db_model = BookingsOrm
    schema = Booking

class FacilitiesDataMapper(DataMapper):
    db_model = FacilitiesOrm
    schema = Facilities

class RoomFacilitiesDataMapper(DataMapper):
    db_model = RoomsFacilitiesOrm
    schema = RoomFacilities

