class Bike:
    name = "Mountain Bike"
    gear = 0

bike1 = Bike()

print(bike1.name)

bike1.gear = 5
bike1.name="Road Bike"

print(f"Name: {bike1.name}, Gear: {bike1.gear}")