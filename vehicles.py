# Demonstrate Polymorphism by calling the move() method on both objects
# Base class
class vehicle:
    def move():
        print("The Vehicle is moving.")

# sub class
class Car(vehicle):
    def move(self):
        print("Driving on the road.")

# second sub class
class Bicycle(vehicle):
    def move(self):
        print("Pedaling on the road.")

vehicles = [Car() , Bicycle()]

for v in vehicles:
    v.move()

