from pydantic import BaseModel


class CarCreate(BaseModel):
    model: str
    power: int | None = None
    color: str | None = None

class Car(CarCreate):
    id: int