class inheritance:
    def park(self):
        print("Car Parking")
#child class Dog inherits the base class Animal
class Car(inheritance):
    def runnig(self):
        print("Car Running")
d = Car()
d.runnig()
d.park()