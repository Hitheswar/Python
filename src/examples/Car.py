class Car:
   """Representing Car"""
   def __init__(self,name):
      """Initializing Car Object"""
      self.name = name
   def run(self):
      """SImulate sitting."""
      print(self.name+" is running")

my_car = Car('land_rover')
my_car.run()