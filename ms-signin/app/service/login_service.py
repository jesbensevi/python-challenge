

from app.repository.auth import JWTRepo
from app.repository.users import UsersRepository
from app.schema import LoginSchema
from fastapi import HTTPException
from passlib.context import CryptContext

# Encrypt password
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:

    @staticmethod
    async def logins_service(login: LoginSchema):
        _username = await UsersRepository.find_by_username(login.username)
        if _username is not None:
            if login.password != _username.password:
                raise HTTPException(
                    status_code=400, detail="Invalid Password !")
            return JWTRepo(data={"username": _username.username}).generate_token()
        raise HTTPException(status_code=404, detail="Username not found !")
