class Car:   
    def __init__(self, name, factory, type, fuel):
        self.name = name
        self.factory = factory
        self.type = type
        self.fuel = fuel

    def description(self):
        return f'Car name : {self.name}\nCar factory : {self.factory}\nCar type : {self.type}\nCar fuel : {self.fuel}\nCar on stock!'
    
    def car_run(self, fuel): 
        return f'Car is running\nCar fuel : {self.fuel-10}'

obj2 = Car('Brio','Honda','City car',100)
print(obj2.description())
print(obj2.car_run(100))