from vehicle import RentalVehicle

class RentalBike(RentalVehicle):
    _STORE = "Bike"
    
    # retal price for an hour
    _hourlyRentalPrice = 20
    # retal price for a day
    _dailyRentalPrice = 50

    # if rental time greater than 1 hour
    _hourlyRentalAdditionPrice = _hourlyRentalPrice // 2
    # if rental time greater than 1 day    
    _dailyRentalAdditionPrice = _dailyRentalPrice // 2
    
    def __init__(self, stock):
        super().__init__(stock)


