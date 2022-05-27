from pydantic import BaseModel


class Car(BaseModel):
    brand: str
    model: str
    doors: int

