from typing import Union

from fastapi import FastAPI

from schemas import Car, CarCreate

app = FastAPI()


@app.get("/")
def all_cars() -> list[Car]:
    return [
        Car(id=1, model="Fiat 500", color='rose', power=150),
        Car(id=2, model="Super 5"),
        Car(id=3, model="Ferrari F40", power=400, color="rouge")
    ]


@app.get("/car/{car_id}")
def one_car(car_id: int, q: Union[str, None] = None) -> Car:
    return Car(id=car_id, model="Super Car")

@app.post("/")
def add_car(car: CarCreate):
    return Car(id=1000, model=car.model, color=car.color, power=car.power)