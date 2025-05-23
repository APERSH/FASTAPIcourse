from sqlalchemy import select

from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import UserDataMapper
from src.schemas.users import User, UserWithHashedPassword
from src.models.users import UsersOrm

class UsersRepository(BaseRepository):
    model = UsersOrm
    mapper = UserDataMapper

    async def get_user_with_hashed_password(self, email):
        query = select(self.model).filter_by(email = email)
        result = await self.session.execute(query)
        model = result.scalars().one()
        return UserWithHashedPassword.model_validate(model, from_attributes=True)