from enum import Enum, auto

class Brand(Enum):
    BMW = auto()
    Fiat = auto()
    Ford = auto()
    Kia = auto()
    Porsche = auto()


class Car:
    def __init__ (self, brand, age, maxSpeed, horsePower):
        self.brand = brand
        self.age = age
        self.maxSpeed = maxSpeed
        self.horsePower = horsePower

class Parking:
    

    def __init__(self, max_capacity, cost_per_hour):
        self.cars = []
        self.time_table = {}
        self.history = []
        self.max_capacity = max_capacity
        self.cost_per_hour = cost_per_hour

    def parkCar(self, car, start_hour):

        if len(self.cars) >= self.max_capacity:
            print("Parking is full!")
        else:
            self.cars.append(car)
            self.time_table[car] = start_hour

    def leaveParking(self, car, end_hour):
        self.cars.remove(car)
        start_hour = self.time_table.pop(car)
        record = (car, start_hour, end_hour)
        self.history.append(record)

    def profit(self):

        
        sorted_history = sorted(self.history, key=lambda record: record[2] - record[1])   
        print(sorted_history)

        for record in sorted_history:
            print((record[2] - record[1])*self.cost_per_hour)
    

    def __del__(self):
        print("Parking is closed!")
    

       
if __name__ == "__main__":
    car1 = Car(Brand.BMW, 5, 280, 10)
    car2 = Car(Brand.Fiat, 2, 140, 12)
    car3 = Car(Brand.Ford, 7, 180, 4)
    car4 = Car(Brand.Kia, 12, 120, 3)
    car5 = Car(Brand.Porsche, 1, 300, 12)
    car6 = Car(Brand.Kia, 19, 270, 5)

    parking = Parking(5, 30)
    parking.parkCar(car1, 7)
    parking.parkCar(car2, 6)
    parking.parkCar(car3, 8)
    parking.parkCar(car4, 5)
    parking.parkCar(car5, 15)
    parking.leaveParking(car1, 23)
    parking.leaveParking(car2, 20)
    parking.leaveParking(car3, 22)
    parking.leaveParking(car4, 11)
    parking.leaveParking(car5, 19)
    parking.profit()



        




