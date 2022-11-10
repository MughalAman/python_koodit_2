class Car:
    def __init__(self, license_plate: str, top_speed: int):
        self.license_plate = license_plate
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def __str__(self) -> str:
        return f"License plate: {self.license_plate}, top speed: {self.top_speed} km/h, current speed: {self.current_speed} km/h, distance traveled: {self.distance_traveled} km"


if __name__ == "__main__":
    car1 = Car("ABC-123", 142)
    print(car1)

