class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

    # Encapsulation: Private attribute for brand and model.


class Car(Vehicle):
    def move(self):
        print("The car is moving on the road.")


class Boat(Vehicle):
    def move(self):
        print("The boat is sailing on the water.")


class Plane(Vehicle):
    def move(self):
        print("The plane is flying in the sky.")


def demonstrate_movement(Vehicle):
    Vehicle.move()
    print("The vehicle is in motion.")


# Example usage:
my_car = Car()
my_boat = Boat()
my_plane = Plane()

demonstrate_movement(my_car)  # Output: The car is moving on the road.
demonstrate_movement(my_boat)  # Output: The boat is sailing on the water.
demonstrate_movement(my_plane)  # Output: The plane is flying in the sky.
# The code demonstrates polymorphism by allowing different types of vehicles
# to be moved using the same method.
