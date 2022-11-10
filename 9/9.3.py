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
        return f"License plate: {self.license_plate}, top speed: {self.top_speed} km/h, current speed: {self.current_speed} km/h, distance traveled: {self.distance_traveled:0.0f} km"


if __name__ == "__main__":
    car1 = Car("ABC-123", 142)
    car1.accelerate(60)
    car1.distance_traveled = 2000
    car1.move(1.5)
    print(car1)


