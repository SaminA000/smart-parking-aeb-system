class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mph = 0

    def get_full_info(self):
        return f"{self.year} {self.make} {self.model}"
    def get_car_info(self):
        return f"{self.make} {self.model}"
    
    def accelerate(self, amount):
        print(f"{self.get_car_info()} is accelerating.")
        self.mph += amount
