#create a simple class hierarchy involving a vehicle class as the base class and two subclasses car and bike.
#show how you would implement a method in the base class and override it in the subclasses.

# Base class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print(f"The {self.brand} vehicle's engine is starting...")

# Subclass Car
class Car(Vehicle):
    def start_engine(self):
        print(f"The {self.brand} car's engine roars to life with a smooth hum.")

# Subclass Bike
class Bike(Vehicle):
    def start_engine(self):
        print(f"The {self.brand} bike's engine starts with a loud vroom!")

# Example usage
vehicle = Vehicle("Generic")
car = Car("Toyota")
bike = Bike("Harley-Davidson")

vehicle.start_engine()  # Calls base class method
car.start_engine()      # Calls overridden method in Car
bike.start_engine()     # Calls overridden method in Bike

