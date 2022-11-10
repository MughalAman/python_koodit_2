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

class Race:
    def __init__(self, name: str, length: int, cars: list[Car]):
        self.name = name
        self.length = length
        self.cars = cars

    def race_over(self) -> bool:
        for car in self.cars:
            if car.distance_traveled >= self.length:
                return True
        return False

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 10))
            car.move(1)

    def print_status(self):
        for car in self.cars:
            print(car)



if __name__ == "__main__":
    cars_list = []
    hours_passed = 0

    for i in range(10):
        cars_list.append(Car(f"ABC-{i + 1}", random.randint(100, 200)))

    race = Race("Suuri romuralli", 8000, cars_list)

    while not race.race_over():
        race.hour_passes()
        hours_passed += 1

        if hours_passed == 10:
            race.print_status()
            hours_passed = 0

    race.print_status()