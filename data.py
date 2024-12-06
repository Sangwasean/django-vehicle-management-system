from vehicles.models import Vehicle
from random import choice, randint
from decimal import Decimal
from datetime import date
import random

# Define sample data
manufacturers = ["Toyota", "Ford", "BMW", "Mercedes", "Honda", "Nissan", "Chevrolet", "Volkswagen", "Audi", "Hyundai"]
body_types = ["Sedan", "SUV", "Truck", "Coupe", "Convertible", "Hatchback", "Van", "Wagon"]
engine_types = ["petrol", "diesel", "electric"]
transmissions = ["manual", "automatic"]
fuel_types = ["gasoline", "diesel", "electric", "hybrid", "biodiesel", "hydrogen", "ethanol"]
statuses = ["active", "inactive", "sold"]
colors = [
    "black", "white", "silver", "gray", "red", "blue", "green", "yellow", "brown", "orange",
    "purple", "metallic_black", "metallic_silver", "metallic_gray", "metallic_red",
    "metallic_blue", "metallic_green", "metallic_brown", "pearl_white", "matte_black",
    "chrome", "gold", "custom"
]

# Create 20 Vehicle objects
vehicles = []
for _ in range(100000):
    vin = ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for _ in range(17))
    manufacturer = choice(manufacturers)
    year = randint(1990, 2024)
    color = choice(colors)
    body_type = choice(body_types)
    engine_type = choice(engine_types)
    transmission = choice(transmissions)
    fuel_type = choice(fuel_types)
    seating_capacity = randint(2, 10)
    price = Decimal(f"{randint(20000, 80000)}.99")
    status = choice(statuses)
    registration_date = date(randint(2000, 2023), randint(1, 12), randint(1, 28))
    vehicle = Vehicle(vin=vin, manufacturer=manufacturer, year=year, color=color, body_type=body_type, engine_type=engine_type, transmission=transmission, fuel_type=fuel_type, seating_capacity=seating_capacity, price=price, status=status, registration_date=registration_date)
    vehicles.append(vehicle)
    print("vehicle added")
Vehicle.objects.bulk_create(vehicles)



