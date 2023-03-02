

from app.repository.auth import JWTRepo
from app.repository.users import UsersRepository
from app.schema import LogoutSchema
from fastapi import HTTPException


class AuthService:

    @staticmethod
    async def logouts_service(logout: LogoutSchema):
        _username = await UsersRepository.find_by_username(logout.username)
        if _username is None:
            raise HTTPException(
                status_code=400, detail="Username not found !")
        return _username
