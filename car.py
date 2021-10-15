class Car():

    def __init__(self,make,model,year) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.odometar_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometar(self):
        print("This car has " +str(self.odometar_reading) + " miles on it.")    
    
    def update_odometar(self,mileage):
        if mileage >= self.odometar_reading:
            self.odometar_reading =mileage
        else:
            print("Cant rollback odometar!")
    def increment_odometar(self,miles):
        self.odometar_reading += miles

class ElectricCar(Car):
    def __init__(self, make, model, year) -> None:
        super().__init__(make, model, year)

        
my_tesla= ElectricCar('tesla','model s',2015)
print(my_tesla.get_descriptive_name())

"""my_new_car = Car ("audi","a4",2018)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometar()"""



