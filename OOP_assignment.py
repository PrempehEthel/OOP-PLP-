# This code demonstrates the use of inheritance in Python
# by creating a base class
# `Smartphone` and two derived classes
# `SmartphoneWithCamera` and `SmartphoneWithGPS`.


class Smartphone:
    def __init__(self, brand, model, storage_capacity, battery_life):
        # Encapsulation: Private attributes are used to hide
        # the internal state of the object.
        self._brand = brand
        self._model = model
        self._storage_capacity = storage_capacity
        self._battery_life = battery_life

    def make_call(self, contact):
        # Polymorphism:
        # This method can be used by any derived class without modification.
        print(f"Calling {contact}... from {self._brand} {self._model}.")

    def check_battery(self):
        # Polymorphism: This method can also be used by any derived class.
        print(f"Battery life: {self._battery_life} hours remaining.")


# defining the derived class SmartphoneWithCamera
# which inherits from the base class Smartphone
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, storage_capacity, battery_life, camera_resolution):
        super().__init__(brand, model, storage_capacity, battery_life)
        # Encapsulation: Private attribute for camera resolution.
        self._camera_resolution = camera_resolution

    def take_photo(self):
        # Polymorphism: This method is specific to this class and can be used by derived classes.
        print(
            f"Taking a photo with {self._camera_resolution} MP camera on {self._brand} {self._model}."
        )

    def record_video(self):
        # Polymorphism: This method is specific to this class and can be used by derived classes.
        print(
            (
                f"Recording video with {self._camera_resolution} MP camera on "
                f"{self._brand} {self._model}."
            )
        )


# defining the derived class SmartphoneWithGPS
# which inherits from the base class Smartphone
class SmartphoneWithGPS(Smartphone):
    def __init__(self, brand, model, storage_capacity, battery_life):
        super().__init__(brand, model, storage_capacity, battery_life)
        # Encapsulation: Private attribute for GPS functionality.
        self._gps_enabled = True

    def get_location(self):
        # Polymorphism: This method is specific to this class a
        # nd can be used by derived classes.
        print(f"Getting location using GPS on {self._brand} {self._model}.")


# defining the derived class SmartphoneWithCameraAndGPS
# which inherits from both SmartphoneWithCamera and SmartphoneWithGPS
class SmartphoneWithCameraAndGPS(SmartphoneWithCamera, SmartphoneWithGPS):
    def __init__(self, brand, model, storage_capacity, battery_life, camera_resolution):
        # Polymorphism: Calls the constructors of both parent classes.
        SmartphoneWithCamera.__init__(
            self, brand, model, storage_capacity, battery_life, camera_resolution
        )
        SmartphoneWithGPS.__init__(self, brand, model, storage_capacity, battery_life)


# Example usage:
my_iphone = SmartphoneWithCameraAndGPS("Apple", "iPhone 14", "128GB", 20, 12)

# Polymorphism: The following methods demonstrate polymorphic behavior.
my_iphone.make_call("John Doe")  # Inherited from Smartphone
my_iphone.check_battery()  # Inherited from Smartphone
my_iphone.take_photo()  # Inherited from SmartphoneWithCamera
my_iphone.record_video()  # Inherited from SmartphoneWithCamera
my_iphone.get_location()  # Inherited from SmartphoneWithGPS
