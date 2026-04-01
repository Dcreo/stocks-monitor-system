from pydantic import BaseModel

class LoginDTO(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
