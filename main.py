from customer import Customer
from bike import RentalBike

rental_bike = RentalBike(20)
customer = Customer()

while True:
    print("""
        Menue:
            A. Display available bikes
            B. Display your state
            C. Request for rent a bike on hourly (${})
            D. Request for rent a bike on daily (${})
            E. Return and pay bill
            F. Exit
    """.format(rental_bike._hourlyRentalPrice, rental_bike._dailyRentalPrice))
    
    chose = input(">>>")

    if chose == "A" or chose == "a":
        rental_bike.displayEnventory()

    elif chose == "B" or chose == "b":
        customer.displayState()

    elif chose == "C" or chose == "c":
        rental_bike.rentOnHourly(customer.request(), customer)  

    elif chose == "D" or chose == "d":
        rental_bike.rentOnDaily(customer.request(), customer)
                  
    elif chose == "E" or chose == "e":
        rental_bike.returnAndPayBill(customer.returnBike())
        customer.bikes, customer.rentalTimeFrom, customer.rentalType = 0, 0, 0
    
    elif chose == "F" or chose == "f":
        break
    else:
        print("Invalid Input: your input must be a, b, c, d or f!")
