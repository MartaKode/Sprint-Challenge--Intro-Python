# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

#base class Vehicle:
class Vehicle:
    pass

# children of vehicle 
class FlightVehicle(Vehicle):
    pass
class GroundVehicle(Vehicle):
    pass

# children of FLight Vehicle
class Starship(FlightVehicle):
    pass
class Airplane(FlightVehicle):
    pass

#children of Ground Vehicle:
class Car(GroundVehicle):
    pass
class Motorcycle(GroundVehicle):
    pass