class Car:
    def __init__(self, car_id):
        self.car_id = car_id

class CarPark:
    def __init__(self, capacity):
        self.capacity = capacity
        self.parking_spaces = capacity
        self.carpark = []
        self.queue = []

    def car_arrived(self, car_id):
        if self.parking_spaces > 0:
            self.parking_spaces -= 1
            self.carpark.append(Car(car_id))
            return f"Car {car_id} entered the car park."
        else:
            self.queue.append(Car(car_id))
            return f"Car {car_id} joined the queue."

    def car_departed(self):
        if self.parking_spaces < self.capacity:
            self.parking_spaces += 1
            if self.queue:
                cur_car = self.carpark.pop(0)
                next_car = self.queue.pop(0)
                self.parking_spaces -= 1
                return cur_car.car_id, f"Car {next_car.car_id} exited the queue and entered the car park."
            else:
                return None, "A car exited the car park."
        else:
            return None, "No cars in the car park to exit."