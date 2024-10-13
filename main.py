class WaterPump:

    def __init__(self, power_consumption=0, brand="", volume_ph=0, price=0, name=""):
        self.__power_consumption = power_consumption 
        self.__brand = brand
        self.__volume_ph = volume_ph
        self.price = price
        self.name = name


    
    def get_power_consumption(self):
        return self.__power_consumption

    def get_brand(self):
        return self.__brand

    def get_volume_ph(self):
        return self.__volume_ph



    def __str__(self):
        return f"{self.__power_consumption}, {self.__brand}, {self.__volume_ph}, {self.price}, {self.name}"

    def __repr__(self):
        return f"WaterPump(power_consumption='{self.__power_consumption}', brand='{self.__brand}', volume_ph='{self.__volume_ph}', price='{self.price}', name='{self.name}')"


    def __del__ (self):
        print("WaterPump destroyed")


def main():
    waterpump_default = WaterPump()
    waterpump_ultra = WaterPump(480, "Amio", 80, 3000, "Water pump superultra")
    waterpump_samsung = WaterPump(500, "Samsung", 100, 4500, "Water pump FE23")
    waterpumps = [waterpump_default, waterpump_ultra, waterpump_samsung]
    for waterpump in waterpumps:
        print("Using string: ", str(waterpump))
        print("Using repr: ", repr(waterpump))
    

if __name__ == "__main__":
    main()
    
    



