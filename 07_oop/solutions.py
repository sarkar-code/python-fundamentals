class Car:
    total_car = 0

    def __init__( self, userbrand, usermodel):
        self.__brand = userbrand
        self.__model = usermodel
        Car.total_car += 1

    def get_brand(Self):
        return Self.__brand + " !"

    def full_name(self):
        return f" {self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are mean of transport"
    
    @property
    def get_model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, userbrand, usermodel, battery_size):
        super().__init__(userbrand, usermodel)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric charge"

# my_tesla =ElectricCar("Tesla", "Model S", "85kWh")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))
# print(my_tesla.battery_size)
# print(my_tesla.__brand)#direct access not possible
# print(my_tesla.get_brand())
# print(my_tesla.full_name())
# print(my_tesla.fuel_type())

# safari = Car("TATA", "Safari")

# print(safari.get_model())


# Car("TATA", "Nexon")# we can also use without variable
#  print(safari.fuel_type())

# print(Car.general_description())
# print(safari.general_description())

# print(Car.total_car)

# my_car = Car("Toyota", "corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())


# my_new_car = Car("Tata", "Safari")
# print(my_new_car.brand)


class Battery:
    def battery_info(self):
        return "This is Battery"
class Engine:
    def engine_info(Self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())