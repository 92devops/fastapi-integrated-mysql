from pydantic import BaseModel, Field, EmailStr, model_validator, PrivateAttr, ConfigDict
from datetime import datetime
from typing import Optional


class UserRegister(BaseModel):
    name: str = Field(..., title="用户名", max_length=32, min_length=3, description="用户名长度在3~32之间")
    password: str = Field(..., title="密码", gl=5, description="密码长度需要大于5")
    _r_password: str = PrivateAttr(default=None)
    age: int = Field(title="年龄", default=18)
    email: EmailStr
    mobile: str = Field(pattern="1[3|5|7|6|8]\d{9}")
    isDelete: bool = False
    created_at: datetime = None

    @model_validator(mode='before')
    def validate_userinfo_password(self):
        if self.get("password") != self.get("r_password"):
            raise ValueError("二次密码不匹配")
        return self

class UserUpdate(BaseModel):
    """
    更新用户记录时候需要传递参数信息
    """
    name: Optional[str]
    age:  Optional[int]
    email:  Optional[EmailStr]
    mobile: Optional[str]
    isDelete: bool

class UserOut(BaseModel):
    id: int
    name: str = Field(..., title="用户名",max_length=32, min_length=3, description="用户名长度在3~32之间")
    age: int = Field(title="年龄", default=18)
    email: EmailStr
    mobile: str
    isDelete: bool
    created_at: datetime =None

    model_config = ConfigDict(from_attributes=True)
