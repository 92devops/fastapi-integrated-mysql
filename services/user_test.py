from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from dependencies import get_db
from models.user import  User
from db.database import engine, Base
from schemas.user import UserRegister, UserUpdate, UserOut


class UserService:

    """创建表"""
    @staticmethod
    async def init_table():
        async with engine.begin() as conn:
            # await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    """创建用户"""
    @staticmethod
    async def create_user(db: AsyncSession, **kwargs):
        new_user = User(**kwargs)
        db.add(new_user)
        await  db.commit()
        return new_user


    """获取用户列表"""
    @staticmethod
    async def get_users(db: AsyncSession):
        users = db.query(User).all()
        return users

    """获取用户详情"""
    @staticmethod
    async def get_user(user_id:int, db: AsyncSession = Depends(get_db)):
        user = db.query(User).filer(User.id == user_id).first()
        if not  user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="用户不存在")
        return user

    """更新用户"""
    @staticmethod
    async def update_user(user_id:int, user:UserUpdate, db: AsyncSession):
        user_query = db.query(User).filer(User.id == user_id)
        if not  user_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="用户不存在")
        user_query.update(user.dict(), synchronize_session=False)
        await db.commit()
        return user_query.first()

    """删除用户"""
    @staticmethod
    async def delete(user_id:int,  db: AsyncSession):
        user_query = db.query(User).filer(User.id == user_id)
        if not  user_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="用户不存在")
        user_query.delete(synchronize_session=False)
        await db.commit()
        return user_query.first()





