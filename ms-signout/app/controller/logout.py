
from app.schema import LogoutSchema, ResponseSchema
from app.service.logout_service import AuthService
from fastapi import APIRouter, Depends, Request
from fastapi_jwt_auth import AuthJWT

router = APIRouter(prefix="/signout", tags=['Authentication'])


@router.post("")
async def login(requset_body: LogoutSchema, request: Request, Authorize: AuthJWT = Depends()):
    if request.headers.get('Cookie') is None:
        return ResponseSchema(detail="Not Set Cookie", result={"Cookie": "Not Cookie"})
    user = await AuthService.logouts_service(requset_body)
    Authorize.unset_jwt_cookies()
    return ResponseSchema(detail="Successfully logout", result={"Cookie": "Unset Cookie"}) 
