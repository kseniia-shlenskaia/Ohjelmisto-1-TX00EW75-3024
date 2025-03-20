class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        new_speed = self.speed + change_of_speed
        if new_speed > self.maximum_speed:
            self.speed = self.maximum_speed
        elif new_speed < 0:
            self.speed = 0
        else:
            self.speed = new_speed

new_car = Car('ABC-123', 142)

new_car.accelerate(30)
print(f"The current speed of a car is {new_car.speed} km/h")
new_car.accelerate(70)
print(f"The current speed of a car is {new_car.speed} km/h")
new_car.accelerate(50)
print(f"The current speed of a car is {new_car.speed} km/h")
new_car.accelerate(-200)
print(f"The final speed of a car is {new_car.speed} km/h")
