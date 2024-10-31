from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    phone_dial_code: str
