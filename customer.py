import datetime

class Customer:
    def __init__(self):
        self.__bikes = 0
        self.__rentalTimeFrom = 0
        
        # if __rentalType = 1:Hourly, 2:Daily (this benchmark useful when we want return bikes)
        self.__rentalType = 0

    @property
    def bikes(self): 
        return self.__bikes
    @bikes.setter
    def bikes(self, val):
        if type(val) is not int and val < 0:
            raise Exception("Value for assing Customer.__bikes must be integer 0 or greater than 0")
        self.__bikes = val
    
    @property
    def rentalTimeFrom(self):
        return self.__rentalTimeFrom
    @rentalTimeFrom.setter
    def rentalTimeFrom(self, val):
        if val != 0 and  not isinstance(val, datetime.datetime):
            raise Exception("Value for assing Customer.__rentalTimeFrom must be 0 or instance of datetime.datetime")
        self.__rentalTimeFrom = val

    @property
    def rentalType(self):
        return self.__rentalType
    @rentalType.setter
    def rentalType(self, val):
        if val != 0 and val != 1 and val != 2:
            raise Exception("Value for assing Customer.__rentalType must be 0, 1 or 2!")
        self.__rentalType = val




    def displayState(self):
        if self.__bikes and self.__rentalTimeFrom and self.__rentalType:
            rentalType = "Hourly" if self.__rentalType == 1 else "Daily"
            print("You rented {} bike(s) on {} at {}:{}".format(self.__bikes, rentalType, self.__rentalTimeFrom.hour, self.__rentalTimeFrom.minute))
            return self.__bikes
        else:
            print("You don't have any rented bike!")
            return None

    def request(self):
        if self.__bikes and self.__rentalTimeFrom and self.__rentalType:
            print("You rent {} bike(s) at {}:{}, so you can't rent a bikes again!".format(
                    self.__bikes, 
                    self.__rentalTimeFrom.hour, 
                    self.__rentalTimeFrom.minute))
            return None
        bikes = input("How many bike would you like to rent? ")
    
        try:
            bikes = int(bikes)
        except ValueError:
            print("ERR: Your input must be integer.")
            return None
    
        else:
            if bikes < 1:
                print("Your input must be greater than zero!")
                return None
            return bikes

    def returnBike(self):
        if self.__bikes and self.__rentalTimeFrom and self.__rentalType:
            return (self.__bikes, self.__rentalTimeFrom, self.__rentalType)
        else:
            return (0, 0, 0)
