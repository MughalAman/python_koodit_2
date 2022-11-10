class Elevator:
    def __init__(self, bottom_floor: int, top_floor: int):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f'Current floor: {self.current_floor}')

    def go_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f'Current floor: {self.current_floor}')

    def go_to(self, floor: int):
        if self.current_floor < floor:
            while self.current_floor < floor:
                self.go_up()
        elif self.current_floor > floor:
            while self.current_floor > floor:
                self.go_down()

class House:
    def __init__(self, bottom_floor: int, top_floor: int, elevators: int):
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(elevators)]

    def move_elevator(self, elevator: int, floor: int):
        if 0 <= elevator < len(self.elevators):
            print(f'\nMoving elevator {elevator} to floor {floor}')
            self.elevators[elevator].go_to(floor)

    def fire_alarm(self):
        print('\nFire alarm!')
        for elevator_number, elevator in enumerate(self.elevators):
            print(f'\nMoving elevator {elevator_number} to bottom floor!')
            elevator.go_to(elevator.bottom_floor)

if __name__ == '__main__':
    house = House(0, 10, 3)
    house.move_elevator(0, 5)
    house.move_elevator(1, 3)
    house.move_elevator(2, 7)
    house.fire_alarm()