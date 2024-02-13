from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

from domain.car import Car, CarPark
from config import PARK_CAPACITY

app = FastAPI()


car_park = CarPark(capacity=PARK_CAPACITY)

@app.post("/car/enter")
def enter_car(car_id: str) -> str:
    car = Car(car_id)
    return car_park.car_arrived(car.car_id)

@app.post("/car/exit")
def exit_car() -> str:
    car_id, message = car_park.car_departed()
    if car_id:
        return f"Car {car_id} exited the car park. " + message
    else:
        return message
@app.get("/carpark/status")
def carpark_status() -> Dict:
    return {
        "parking_spaces": car_park.parking_spaces,
        "queue_size": len(car_park.queue)
    }
