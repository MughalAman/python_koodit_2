import random

class Car:
    def __init__(self, license_plate: str, top_speed: int):
        self.license_plate = license_plate
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance_traveled = 0
    
    def accelerate(self, speed: int):
        if speed > 0:
            if self.current_speed + speed > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += speed

        elif speed < 0:
            if self.current_speed + speed < 0:
                self.current_speed = 0
            else:
                self.current_speed += speed

    def move(self, time: int):
        self.distance_traveled += self.current_speed * time

    def __str__(self) -> str:
        return f"License plate: {self.license_plate} | top speed: {self.top_speed} km/h | current speed: {self.current_speed} km/h | distance traveled: {self.distance_traveled:0.0f} km"

def check_winner(cars: list[Car]) -> bool:
    for car in cars:
        if car.distance_traveled >= 10000:
            return True


if __name__ == "__main__":
    cars_list = []

    for i in range(10):
        cars_list.append(Car(f"ABC-{i + 1}", random.randint(100, 200)))

    while not check_winner(cars_list):
        for car in cars_list:
            car.accelerate(random.randint(-10, 15))
            car.move(1)

    for car in cars_list:
        print(car)
    


