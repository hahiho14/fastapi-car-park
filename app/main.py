
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Dict

from domain.car import Car, CarPark
from config import ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, \
SECRET_KEY, PARK_CAPACITY, USERS_DB


app = FastAPI()
car_park = CarPark(capacity=PARK_CAPACITY)
users_db = USERS_DB

def authenticate_user(username: str, password: str):
    user = users_db.get(username)
    if not user:
        return False
    if not password == user["password"]:
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username

@app.post("/token")
async def login(form_data: dict):
    user = authenticate_user(form_data["username"], form_data["password"])
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": form_data["username"]}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/car/enter")
def enter_car(car_id: str, current_user: str = Depends(get_current_user)) -> str:
    user_role = current_user.get("role")
    if user_role != "admin":
        raise HTTPException(status_code=403, detail="Permission denied")
    car = Car(car_id)
    return car_park.car_arrived(car.car_id)

@app.post("/car/exit")
def exit_car(current_user: str = Depends(get_current_user)) -> str:
    user_role = current_user.get("role")
    if user_role != "admin":
        raise HTTPException(status_code=403, detail="Permission denied")
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
