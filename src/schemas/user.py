from pydantic import BaseModel

class UserDTO(BaseModel):
    id: int
    username: str
    email: str

    class ConfigDict:
        from_attributes = True

class UserCreateDTO(BaseModel):
    username: str
    password: str
    email: str
