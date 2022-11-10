class Car:
    def __init__(self, license_plate: str, top_speed: str):
        self.license_plate = license_plate
        self.top_speed = top_speed.split(" ")[0]
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

class ElectricCar(Car):
    def __init__(self, license_plate: str, top_speed: str, battery_capacity: str):
        super().__init__(license_plate, top_speed)
        self.battery_capacity = battery_capacity

    def __str__(self) -> str:
        return f"License plate: {self.license_plate} | top speed: {self.top_speed} km/h | current speed: {self.current_speed} km/h | distance traveled: {self.distance_traveled:0.0f} km"

class GasCar(Car):
    def __init__(self, license_plate: str, top_speed: str, fuel_capacity: str):
        super().__init__(license_plate, top_speed)
        self.fuel_capacity = fuel_capacity

    def __str__(self) -> str:
        return f"License plate: {self.license_plate} | top speed: {self.top_speed} km/h | current speed: {self.current_speed} km/h | distance traveled: {self.distance_traveled:0.0f} km"




if __name__ == "__main__":
    ec = ElectricCar("ABC-15", "180 km/h", "52.5 kWh")
    gc = GasCar("ACD-123", "165 km/h", "32.3 l")

    ec.current_speed = 150
    gc.current_speed = 100

    ec.move(3)
    gc.move(3)

    print(f"{ec.distance_traveled} km")
    print(f"{gc.distance_traveled} km")