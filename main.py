import datetime


class BikeRental:
    def __init__(self, stock=0):
        """
        Our constructor class that instantiates bike rental shop.
        """
        self.stock = stock

    def displayStock(self):
        """
        Displays the bikes currently available for rent in the shop.
        """
        print("We have currently {} bikes available to     rent.".format(self.stock))

    def rentBikeOnHourlyBasis(self, n):
        """
        Rents a bike on hourly basis to a customer.
        """
        if n <= 0:
            print('Number of bike(s) should be positive')
            return None
        elif n > self.stock:
            print("We have {} bike(s) available to rent".format(self.stock))
            return None
        else:
            now = datetime.datetime.now()
            print("You have rented a {} bike(s) on hourly basis today at {} hours".format(n, now.hour))
            print("You will be charged $5 for each hour per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= n
            return now

    def rentBikeOnDailyBasis(self, n):
        """
        Rents a bike on daily basis to a customer.
        """
        if n <= 0:
            print('Number of bike(s) should be positive')
            return None
        elif n > self.stock:
            print("We have {} bike(s) available to rent".format(self.stock))
            return None
        else:
            now = datetime.datetime.now()
            print("You have rented a {} bike(s) on daily basis today at {} hours".format(n, now.hour))
            print("You will be charged $20 for each day per bike.")
            print("We hope that you enjoy our service.")

            self.stock -= n
            return now

    def rentBikeOnWeeklyBasis(self, n):
        """
        Rents a bike on daily basis to a customer.
        """
        if n <= 0:
            print('Number of bike(s) should be positive')
            return None
        elif n > self.stock:
            print("We have {} bike(s) available to rent".format(self.stock))
            return None
        else:
            now = datetime.datetime.now()
            print("You have rented a {} bike(s) on weekly basis today at {} hours".format(n, now.hour))
            print("You will be charged $60 for weel day per bike.")
            print("We hope that you enjoy our service.")

            self.stock -= n
            return now

    def returnBike(self, request):
        """
        1. Accept a rented bike from a customer
        2. Replensihes the inventory
        3. Return a bill
        """

        # extract the tuple and initiate bill
        rentalTime, rentalBasis, numOfBikes = request
        bill = 0

        # issue a bill only if all three parameters are not null!
        if rentalBasis and rentalTime and numOfBikes:
            self.stock += numOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime

            # hourly bill calculation
            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 5 * numOfBikes

            # daily bill calculation
            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) * 20 * numOfBikes

            # weekly bill calculation
            elif rentalBasis == 3:
                bill = round(rentalPeriod.days / 7) * 60 * numOfBikes

            # family discount calculation
            if (3 <= numOfBikes <= 5):
                print("You are eligible for Family rental promotion of 30% discount")
                bill = bill * 0.7
                print("Thanks for returning your bike. Hope you enjoyed our service!")

                print("That would be ${}".format(bill))
                return bill
        else:
            print("Are you sure you want rent bike form us?")
            return None

class Customer:
    def __init__(self) -> None:
        """
        Our constructor method which instantiates various customer objects.
        """

        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    def requestBike(self):
        """
        Takes a request from the customer for the number of bikes.
        """

        bikes = input('How many bike(s) would you like to rent: ')

        try:
            bikes = int(bikes)
        except ValueError:
            print('That\'s not a positive integer')
            return -1
        if bikes < 1:
            print("Invalid Input. Number of bikes should be greater then Zero")
            return -1
        else:
            self.bikes = bikes
            return self.bikes

    def returnBike(self):
        """
        Allows customers to return their bikes to the rental shop.
        """

        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes
        else:
            return 0, 0, 0


    

if __name__ == '__main__':
    
    shop = BikeRental(50)
    customer = Customer()
    shop.displayStock()
    ch = input('Choose your options. 1. Hourly, 2. Daily, 3. Weekly, 4. Return Bike(s): ').lower()
    if ch == 'hourly':
        n = input('How many bike(s) do you want to rent? ')
        try:
            n = int(n)
        except ValueError:
            print('Type a integer')
        shop.rentBikeOnHourlyBasis(n)
    elif ch == 'daily':
        n = input('How many bike(s) do you want to rent? ')
        try:
            n = int(n)
        except ValueError:
            print('Type a integer')
        shop.rentBikeOnDailyBasis(n)
    elif ch == 'weekly':
        n = input('How many bike(s) do you want to rent? ')
        try:
            n = int(n)
        except ValueError:
            print('Type a integer')
        shop.rentBikeOnWeeklyBasis(n)

    elif ch == 'return bike':
        
        request = customer.returnBike()
        shop.returnBike(request)
    # customer = Customer()
    # ch = input('Choose an option 1. Hourly, 2. Daily, 3. Weekly')
    # customer.rentalBasis = ch
    # customer.rentalTime = datetime.datetime.now()
    # request = customer.returnBike()
    # shop.returnBike(request)
    