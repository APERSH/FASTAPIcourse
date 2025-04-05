from repositories.base import BaseRepository
from schemas.users import User
from src.models.users import UsersOrm

class UsersRepository(BaseRepository):
    model = UsersOrm
    schema = User