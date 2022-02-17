from pydantic import BaseModel
from .db import Base


class Address(BaseModel):
    first_name: str
    last_name: str
    street: str
    city: str
    state: str
    zip: str
    lat: float
    lng: float

    class Config():
        orm_mode = True