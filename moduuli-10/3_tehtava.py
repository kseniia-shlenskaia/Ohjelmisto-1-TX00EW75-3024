class Elevator:
    def __init__(self, bottom_floor, top_floor):
        if bottom_floor > top_floor:
            print('Wrong input. The bottom floor cannot be higher than the top floor')

        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.floor = bottom_floor

    def go_to_floor(self, new_floor):
        if not (self.bottom_floor <= new_floor <= self.top_floor):
            print(f'Wrong input. The elevator cannot go below the bottom floor {self.bottom_floor} or above the top floor {self.top_floor}')
            return

        if new_floor == self.floor:
            print(f"The elevator is already on floor number {self.floor}")
            return

        while new_floor != self.floor:
            if new_floor > self.floor:
                self.floor_up()
            elif new_floor < self.floor:
                self.floor_down()

    def floor_up(self):
        self.floor += 1
        print(f"The elevator is on floor number {self.floor}")

    def floor_down(self):
        self.floor -= 1
        print(f"The elevator is on floor number {self.floor}")

class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.list_of_elevators = []
        self.bottom_floor = bottom_floor
        self.top_floor = bottom_floor

        for index in range(number_of_elevators):
            self.list_of_elevators.append(Elevator(self.bottom_floor, self.top_floor))

    def run_elevator(self, number_of_elevator, destination_floor):
        if number_of_elevator < 1 or number_of_elevator > len(self.list_of_elevators):
            print(f"Wrong input. There is no elevator with number {number_of_elevator}")
            return

        selected_elevator = self.list_of_elevators[number_of_elevator - 1]
        print(f"\nThe elevator number {number_of_elevator} is selected on floor number {selected_elevator.floor}")
        selected_elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        print('\nFire alarm!')
        for index in range(len(self.list_of_elevators)):
            number_of_elevator = index + 1
            self.run_elevator(number_of_elevator, self.bottom_floor)

building = Building(1, 10, 2)
building.run_elevator(1, 5)
building.run_elevator(2, 4)

building.fire_alarm()
