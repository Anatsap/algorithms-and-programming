from enum import Enum, auto
from datetime import datetime, timedelta

class Brand(Enum):
    BMW = auto()
    Fiat = auto()
    Ford = auto()
    Kia = auto()
    Porsche = auto()


class Car:
    def __init__ (self, brand, age, maxSpeed, horsePower, plate):
        self.brand = brand
        self.age = age
        self.maxSpeed = maxSpeed
        self.horsePower = horsePower
        self.__plate = plate


    def get_plate(self):
        return self.__plate
    def __str__(self):
        return f"{self.brand}, {self.age}, {self.maxSpeed}, {self.horsePower}, {self.__plate}\n"

    def __repr__(self):
        return f"Car(brand='{self.brand}', age='{self.age}', maxSpeed='{self.maxSpeed}', horsePower='{self.horsePower}', plate='{self.__plate}')\n"


class Parking:
    

    def __init__(self, max_capacity, cost_per_hour, max_speed, price_increase):
        self.price_increase = price_increase
        self.max_speed = max_speed
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

        for record in sorted_history:
            price = (record[2] - record[1]).total_seconds() / 3600 * self.cost_per_hour
            
            if record[0].maxSpeed > self.max_speed :
                price = price + 0.01 * price * self.price_increase
            print(price)
    

    def __del__(self):
        print("Parking is closed!")
    

       
if __name__ == "__main__":
    car1 = Car(Brand.BMW, 5, 280, 10, 9999)
    car2 = Car(Brand.Fiat, 2, 140, 12, 8976)
    car3 = Car(Brand.Ford, 7, 180, 4, 9076)
    car4 = Car(Brand.Kia, 12, 120, 3, 3040)
    car5 = Car(Brand.Porsche, 1, 300, 12, 2024)
    car6 = Car(Brand.Kia, 19, 270, 5, 7588)

    parking = Parking(5, 30, 150, 10)
    parking.parkCar(car1, datetime.fromisoformat('2024-10-26 00:05:23'))
    parking.parkCar(car2, datetime.fromisoformat('2024-10-05 00:11:20'))
    parking.parkCar(car3, datetime.fromisoformat('2024-10-12 00:19:28'))
    parking.parkCar(car4, datetime.fromisoformat('2024-11-07 00:08:03'))
    parking.parkCar(car5, datetime.fromisoformat('2024-12-13 00:16:54'))
    parking.leaveParking(car1, datetime.fromisoformat('2024-10-29 00:19:20'))
    parking.leaveParking(car2, datetime.fromisoformat('2024-10-12 00:07:39'))
    parking.leaveParking(car3, datetime.fromisoformat('2024-11-03 00:10:09'))
    parking.leaveParking(car4, datetime.fromisoformat('2024-12-01 00:22:22'))
    parking.leaveParking(car5, datetime.fromisoformat('2024-12-28 00:18:46'))

    parking.profit()


    



        




