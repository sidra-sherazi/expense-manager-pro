from pydantic import BaseModel, EmailStr, ConfigDict


class UserRegister(BaseModel):
    name: str
    username: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = ConfigDict(
        from_attributes=True
    )