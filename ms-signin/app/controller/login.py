
from app.schema import LoginSchema, ResponseSchema
from app.service.login_service import AuthService
from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT

router = APIRouter(prefix="/signin", tags=['Authentication'])


@router.post("")
async def login(requset_body: LoginSchema, Authorize: AuthJWT = Depends()):
    token = await AuthService.logins_service(requset_body)
    Authorize.set_access_cookies(token)
    return ResponseSchema(detail="Successfully login", result={"token_type": "Bearer", "access_token": token})
