# Vehicle Classes
class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

class Boat:
    def move(self):
        print("Sailing 🚢")


# Animal Classes
class Horse:
    def move(self):
        print("Galloping 🐎")

class Dog:
    def move(self):
        print("Running 🐕")

class Cat:
    def move(self):
        print("Sneaking 🐈")


# Polymorphic function
def perform_move(entity):
    entity.move()


# Create objects
car = Car()
plane = Plane()
boat = Boat()

horse = Horse()
dog = Dog()
cat = Cat()

# Call move() for each object
print("=== Vehicles ===")
perform_move(car)
perform_move(plane)
perform_move(boat)

print("\n=== Animals ===")
perform_move(horse)
perform_move(dog)
perform_move(cat)

