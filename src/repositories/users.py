from sqlalchemy import select

from repositories.base import BaseRepository
from schemas.users import User, UserWithHashedPassword
from src.models.users import UsersOrm

class UsersRepository(BaseRepository):
    model = UsersOrm
    schema = User

    async def get_user_with_hashed_password(self, email):
        query = select(self.model).filter_by(email = email)
        result = await self.session.execute(query)
        model = result.scalars().one()
        return UserWithHashedPassword.model_validate(model, from_attributes=True)