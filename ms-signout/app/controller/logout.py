
from app.schema import LogoutSchema, ResponseSchema
from app.service.logout_service import AuthService
from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT

router = APIRouter(prefix="/signout", tags=['Authentication'])


@router.post("")
async def login(requset_body: LogoutSchema, Authorize: AuthJWT = Depends()):
    user = await AuthService.logouts_service(requset_body)
    Authorize.unset_jwt_cookies()
    return {"msg": "Successfully logout"}
