from fastapi import APIRouter, HTTPException
from starlette import status

from schemas.user import UserRegister, UserOut, UserUpdate
from services.user import UserService
from db.database import AsyncSession
from dependencies import get_db
from fastapi import Depends

router_user = APIRouter(
    prefix="/users",
    tags=["用户管理"]
)

@router_user.post("/", summary="创建用户", status_code=status.HTTP_201_CREATED)
async def create_user(user:UserRegister,db_session: AsyncSession = Depends(get_db)):
    try:
        result= await UserService.create_user(db_session,**user.dict())
        return {"code": "201", "msg": "用户创建成功！","data":result}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"用户创建失败{e}")

@router_user.get("/{user_id}", summary="查询用户详情", status_code=status.HTTP_200_OK)
async def get_user(user_id:int,db_session: AsyncSession = Depends(get_db)):
    usr = await UserService.get_user(db_session,user_id=user_id)
    if usr:
        return {"code": "200", "msg": "查询用户详情成功！", "data": usr}
    else:
        return {"code": "200", "msg": "用户不存在", "data": usr}


@router_user.get("/", summary="获取用户列表", status_code=status.HTTP_200_OK)
async def get_users(db_session: AsyncSession = Depends(get_db)):
    usr = await UserService.get_users(db_session)
    if usr:
        return {"code": "200", "msg": "查询用户列表信息成功！","data":usr}
    else:
        return {"code": "200", "msg": "用户列表为空！","data":usr}


@router_user.put("/{user_id}", summary="修改用户", status_code=status.HTTP_200_OK)
async def edit(user_id: int, user:UserUpdate, db_session: AsyncSession = Depends(get_db)):
    usr = await UserService.get_user(db_session,user_id=user_id)
    if usr:
        print(user.dict())
        usr = await UserService.update_user(user_id, db_session,  **user.dict())
        return {"code": "200", "msg": "修改用户信息成功！", "data": usr}
    else:
        return {"code": "200", "msg": "修改用户信息失败！", "data": None}

@router_user.delete("/{user_id}", summary="删除用户", status_code=status.HTTP_200_OK)
async def delete(user_id:int,db_session: AsyncSession = Depends(get_db)):
    usr = await UserService.get_user(db_session, user_id=user_id)
    if usr:
        return {"code": "200", "msg": "删除用户信息成功！"}
    else:
        return {"code": "200", "msg": "用户不存在"}
