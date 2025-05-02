from fastapi import APIRouter
from src.api.dependencies import DBDep
from src.schemas.facilities import Facilities


router = APIRouter(prefix="/facilities", tags=["Удобства"])

@router.get("")
async def get_facilities(db: DBDep):
    return await db.facilities.get_all()


@router.post("")
async def create_facilities(title: Facilities, db: DBDep):
    facilities = await db.facilities.add(title)
    await db.commit()
    return {"status": "OK", "data": facilities}