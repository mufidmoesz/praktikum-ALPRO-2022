class Car:   
    def __init__(self, name, factory, type, fuel, available):
        self.name = name
        self.factory = factory
        self.type = type
        self.fuel = fuel
        self.available = available

    def description(self):
        return f'Car name : {self.name}\nCar factory : {self.factory}\nCar type : {self.type}\nCar fuel : {self.fuel}\n{self.available}'
    
    def car_run(self, fuel): 
        return f'Car is running\nCar fuel : {self.fuel-10}'

carname = input('Masukkan nama mobil : ')

if carname.lower() == 'brio':
    obj2 = Car('Brio','Honda','City car',100,'Car on Stock!')
    print(obj2.description())
    print('\n')
    print(obj2.car_run(100))
elif carname.lower() == 'crv':
    obj2 = Car('CRV','Honda','SUV',100,'Car is sold')
    print(obj2.description())
    print('\n')
    print(obj2.car_run(100))