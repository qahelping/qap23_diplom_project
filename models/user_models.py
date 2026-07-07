from pydantic import BaseModel, EmailStr, Field, field_validator


class User(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=2, max_length=100)
    email: str
    gender: str
    status: str

    @field_validator("gender")
    @classmethod
    def validate_gender(cls, v: str) -> str:
        if v not in ["male", "female"]:
            raise ValueError('gender должен быть "male" или "female"')
        return v

    @field_validator("status")
    @classmethod
    def validate_status(cls, v: str) -> str:
        if v not in ["active", "inactive"]:
            raise ValueError('status должен быть "active" или "inactive"')
        return v


class UsersResponse(BaseModel):
    users: list[User]


class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    gender: str
    status: str

    @field_validator("gender")
    @classmethod
    def validate_gender(cls, v: str) -> str:
        if v not in ["male", "female"]:
            raise ValueError('gender должен быть "male" или "female"')
        return v

    @field_validator("status")
    @classmethod
    def validate_status(cls, v: str) -> str:
        if v not in ["active", "inactive"]:
            raise ValueError('status должен быть "active" или "inactive"')
        return v


class UserUpdate(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=100)
    email: EmailStr | None = None
    gender: str | None = None
    status: str | None = None

    @field_validator("gender")
    @classmethod
    def validate_gender(cls, v: str | None) -> str | None:
        if v is not None and v not in ["male", "female"]:
            raise ValueError('gender должен быть "male" или "female"')
        return v

    @field_validator("status")
    @classmethod
    def validate_status(cls, v: str | None) -> str | None:
        if v is not None and v not in ["active", "inactive"]:
            raise ValueError('status должен быть "active" или "inactive"')
        return v
