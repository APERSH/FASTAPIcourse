from fastapi import APIRouter, HTTPException, Response


from repositories.users import UsersRepository
from schemas.users import UserAdd, UserRequestAdd
from src.database import async_session_maker
from services.auth import AuthService
from api.dependencies import UserIdDep, DBDep

router = APIRouter(prefix="/auth", tags=["Аавторизация и аутентификация"])


@router.post("/login")
async def login_user(
    data: UserRequestAdd,
    response: Response,
    db: DBDep
):
    user = await db.users.get_user_with_hashed_password(email = data.email)
    if not user:
        raise HTTPException(status_code=401, detail="Пользователь с таким email не зарегистррован")
    if not AuthService().verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Пароль неверный")
    access_token = AuthService().create_access_token({"user_id": user.id})
    response.set_cookie("access_token", access_token)
    return {"access_token": access_token}



@router.post("/register")
async def register_user(
    data: UserRequestAdd,
    db: DBDep
):
    hashed_password = AuthService().hash_password(data.password)
    new_user_data = UserAdd(email = data.email, hashed_password=hashed_password)
    await db.users.add(new_user_data)
    await db.commit()
    return {'status': 'OK'}


@router.get("/me")
async def get_me(
    user_id: UserIdDep,
    db: DBDep
):
    user = await db.users.get_one_or_none(id = user_id)
    return user


@router.get("/logout")
async def logout(response: Response):
    response.delete_cookie("access_token")
    return {'status': 'OK'}
