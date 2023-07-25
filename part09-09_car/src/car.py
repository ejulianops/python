class Car: 
    def __init__(self):
        self.__petrol_in_the_tank = 0
        self.__odometer_reading = 0

    def fill_up(self):
        self.__petrol_in_the_tank = 60

    def drive(self, km:int):
        if km <= self.__petrol_in_the_tank:
            self.__petrol_in_the_tank -= km
            self.__odometer_reading += km
        else:
            self.__odometer_reading -= self.__petrol_in_the_tank
            self.__petrol_in_the_tank = 0
            
    def __str__(self):
        return f"Car: odometer reading {self.__odometer_reading} km, petrol remaining {self.__petrol_in_the_tank} litres"

if __name__ == "__init__":

    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)
