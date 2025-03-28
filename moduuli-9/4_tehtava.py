import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        if not isinstance(change_of_speed, (int, float)):
            print('Wrong input')
            return

        new_speed = self.speed + change_of_speed
        if new_speed > self.maximum_speed:
            self.speed = self.maximum_speed
        elif new_speed < 0:
            self.speed = 0
        else:
            self.speed = new_speed

    def drive(self, hours):
        if not isinstance(hours, (int, float)) or hours < 0:
            print('Wrong input')
            return

        self.travelled_distance += self.speed * hours

list_of_cars = []
for index in range(10):
    car_registration_number = f"ABC-{index + 1}"
    car_maximum_speed = random.randint(100, 200)
    car = Car(car_registration_number, car_maximum_speed)

    list_of_cars.append(car)

while True:
    if any(car.travelled_distance >= 10000 for car in list_of_cars):
        break

    for car_item in list_of_cars:
        car_item.accelerate(random.randint(-10, 15))
        car_item.drive(1)

print(f"{'Registration number':<30}{'Max speed':<20}{'Final speed':<20}{'Travelled distance':<20}")

for car in list_of_cars:
    registration_number = car.registration_number
    maximum_speed = f"{car.maximum_speed} km/h"
    speed = f"{car.speed} km/h"
    travelled_distance = f"{car.travelled_distance} km"
    print(f"{registration_number:<30}{maximum_speed:<20}{speed:<20}{travelled_distance:<20}")
