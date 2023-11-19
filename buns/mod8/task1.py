class Transport():
    def __init__(self, coordinates, speed, brand, year, number):
        self.__coordinates = coordinates
        self.__speed = speed
        self.__brand = brand
        self.__year = year
        self.__number = number
        
    def __str__(self):
        return f"Транспорт: {self.__brand} {self.__number}"
    
    @property
    def coordinates(self):
        return self.__coordinates
    
    @coordinates.setter
    def coordinates(self, coordinates):
        self.__coordinates = coordinates
    
    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, speed):
        self.__speed = speed
    
    @property
    def brand(self):
        return self.__brand
    
    @brand.setter
    def brand(self, brand):
        self.__brand = brand
    
    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, year):
        self.__year = year
    
    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, number):
        self.__number = number
        
    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        pass

class Passenger():
    def __init__(self):
        self.__passengers_capacity = 0
        self.__number_of_passengers = 0
        
    @property
    def passengers_capacity(self):
        return self.__passengers_capacity
        
    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        self.__passengers_capacity = passengers_capacity
        
    @property
    def number_of_passengers(self):
        return self.__number_of_passengers
        
    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        self.__number_of_passengers = number_of_passengers

class Cargo():
    def __init__(self):
        self.__carrying = 0
        
    @property
    def carrying(self):
        return self.__carrying
        
    @carrying.setter
    def carrying(self, carrying):
        self.__carrying = carrying

class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number)
        self.__height = height

class Auto(Transport):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)

class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, name):
        super().__init__(coordinates, speed, brand, year, number)
        self.__name = name

class Car(Auto):
    def __init__(self, coordinates, speed, brand, year, number, body_type):
        super().__init__(coordinates, speed, brand, year, number)
        self.body_type = body_type

class Bus(Auto, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, route_number):
        super().__init__(coordinates, speed, brand, year, number)
        self.route_number = route_number

class CargoAuto(Auto, Cargo):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)

class Boat(Ship):
    def __init__(self, coordinates, speed, brand, year, number, name):
        super().__init__(coordinates, speed, brand, year, number, name)

class PassengerShip(Ship, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, name):
        super().__init__(coordinates, speed, brand, year, number, name)

class CargoShip(Ship, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, name):
        super().__init__(coordinates, speed, brand, year, number, name)

class Seaplane(Plane, Ship):
    def __init__(self, coordinates, speed, brand, year, number, height, name):
        super().__init__(coordinates, speed, brand, year, number, height)
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
