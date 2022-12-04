import datetime

class RentalVehicle:
    _STORE = "Vehicle"

    # retal price for an hour
    _hourlyRentalPrice = 10
    # retal price for a day
    _dailyRentalPrice = 20

    # if rental time greater than 1 hour
    _hourlyRentalAdditionPrice = _hourlyRentalPrice // 2
    # if rental time greater than 1 day    
    _dailyRentalAdditionPrice = _dailyRentalPrice // 2

    def __init__(self, stock):
        self._stock = stock
    
    def displayEnventory(self):
        print("We have currently {} available {}(s) to rent.".format(self._stock, self._STORE))
        return self._stock

    def rentOnHourly(self, n, customer_refrence):
        if n is None:
            return -1
        if n > self._stock:
            print("Sorry! We have currently {} {}(s) available to rent.".format(self._stock, self._STORE))
            return -1
        
        self._stock -= n

        #get time
        now = datetime.datetime.now()

        # set customer attributes
        customer_refrence.bikes = n
        customer_refrence.rentalTimeFrom = now
        customer_refrence.rentalType = 1

        print("You have rented a {} {}(s) on hourly today at {}:{}".format(n, self._STORE, now.hour, now.minute))
        print("If the rental time was more than an hour, you shoud spend {}$ for every 10 minutes".format(self._hourlyRentalAdditionPrice))
        print("We hope that you enjoy our service :)")
        return 1
    
    def rentOnDaily(self, n, customer_refrence):
        if n is None:
            return -1
        if n > self._stock:
            print("Sorry! We have currently {} {}(s) available to rent.".format(self._stock, self._STORE))
            return -1
        

        self._stock -= n

        # get time 
        now = datetime.datetime.now()

        # set customer attributes
        customer_refrence.bikes = n
        customer_refrence.rentalTimeFrom = now
        customer_refrence.rentalType = 2

        print("You have rented a {} {}(s) on daily today at {}:{}".format(n, self._STORE, now.hour, now.minute))
        print("If the rental time was more than a day, you shoud spend {}$ for every 10 minutes".format(self._dailyRentalAdditionPrice))
        print("We hope that you enjoy our service :)")
        return 1

    def returnAndPayBill(self, request):
        """ 
        request is a tuple: (number of bikes, rental time stared from, rental type(Hourly, ...))
        """
        bikes, rentalTime, rentalType = request

        if request == (0, 0, 0):
            print("You don't have any rented bike!")
            return -1

        
        # return bikes to enventory
        self._stock += bikes

        now = datetime.datetime.now()
        delta = now - rentalTime

        # calculate hourly rental
        if rentalType == 1:
            if delta.seconds <= 3600 and delta.days == 0:
                bill = bikes * self._hourlyRentalPrice
                print("You rent {} bikes for {} seconds. your bill is ${}".format(bikes, delta.seconds, bill))
                return bill
            else:
                # first calculate hourly bill
                hourlyBill = bikes * self._hourlyRentalPrice
                
                # حساب کردن ثانیه های اضافی
                newDelta = (delta.days * 86400) + delta.seconds
                newDelta -= 3600

                # تقسیم بر 600 میکنیم تا مشخص بشه چند تا ده دقیقه اضاف اجاره کرده
                tenMinutes = newDelta / 600
                additionBill = bikes * (tenMinutes * self._hourlyRentalAdditionPrice)
                
                total = additionBill + hourlyBill
                
                print("You rent {} bike(s) for {} day(s) and {} seconds.".format(bikes, delta.days, delta.seconds))
                print("your bill for one hour: ${}".format(hourlyBill))
                print("your bill for addition seconds: ${}".format(additionBill))
                print("Total: ${}".format(total))
                return total
        
        # calculate hourly rental
        elif rentalType == 2:
            if (delta.days == 0) or (delta.days == 1 and delta.seconds == 0):
                bill = self._dailyRentalPrice * bikes
                print("You rent {} bikes for 1 day. your bill is ${}".format(bikes, bill))
                return bill
            else:
                dailyBill = self._dailyRentalPrice * bikes

                # حساب کردن ثانیه های اضافی
                newDelta = (delta.days - 1) * 86400
                newDelta += delta.seconds

                # تقسیم بر 600 میکنیم تا مشخص بشه چند تا ده دقیقه اضاف اجاره کرده
                tenMinutes = newDelta  / 600
                additionBill = bikes * (tenMinutes * self._dailyRentalAdditionPrice)

                total = dailyBill + additionBill

                print("You rent {} bike(s) for {} day(s) and {} seconds.".format(bikes, delta.days, delta.seconds))
                print("your bill for a day: ${}".format(dailyBill))
                print("your bill for addition seconds: ${}".format(additionBill))
                print("Total: ${}".format(total))
                return total

