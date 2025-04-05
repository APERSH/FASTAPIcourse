from sqlalchemy import select, insert, update, delete
from pydantic import BaseModel


class BaseRepository:
    model = None

    def __init__(self, session) -> None:
        self.session = session

    async def get_all(self, *args, **kwargs):
        query = select(self.model)
        result = await self.session.execute((query))
        return result.scalars().all()
    
    async def get_one_or_none(self, **filter_by):
        query = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(query)
        return result.scalars().one_or_none()
    
    async def add(self, data: BaseModel):
        add_stat = insert(self.model).values(**data.model_dump()).returning(self.model)
        result = await self.session.execute((add_stat))
        return result.scalars().one()
    
    async def edit(self, data: BaseModel, exclude_unset: bool = False, **filter_by):
        edit_stat = update(self.model).filter_by(**filter_by).values(**data.model_dump(exclude_unset=exclude_unset))
        await self.session.execute(edit_stat)


    async def delete(self, **filter_by):
        delete_stat = delete(self.model).filter_by(**filter_by)
        await self.session.execute(delete_stat)
        
        