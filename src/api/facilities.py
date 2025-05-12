import json

from fastapi import APIRouter
from src.api.dependencies import DBDep
from fastapi_cache.decorator import cache
from src.schemas.facilities import FacilitiesAdd
from src.init import redis_manager


router = APIRouter(prefix="/facilities", tags=["Удобства"])

@router.get("")
@cache(expire=10)
async def get_facilities(db: DBDep):
    return await db.facilities.get_all()

@router.post("")
async def create_facilities(facility_data: FacilitiesAdd, db: DBDep):
    facilities = await db.facilities.add(facility_data)
    await db.commit()
    return {"status": "OK", "data": facilities}