"""
1.created a base class "Vehicle" with attributes model,rental rate and the method calculate_rental
2.Inherited the Vehicle class and created three subclasses Car,Bike and Truck
3.Implemented Polymorphism for calculate_rental method
"""

class Vehicle:
    def __init__(self,model,rental_rate):
        self.model=model
        self.rental_rate=rental_rate
    def calculate_rental(self,type2,duration):
        return self.rental_rate*duration

class Car(Vehicle):
    def __init__(self,model,rental_rate):
        Vehicle.__init__(self,model,rental_rate)
    def calculate_rental(self,type2,duration):
        if type2==1:
            rental=(self.rental_rate * duration) * 1.5
            return rental
        elif type2==2:
            rental=(self.rental_rate*duration)*1.25
            return rental
        else:
            rental=(self.rental_rate*duration)
            return rental

class Bike(Vehicle):
    def __init__(self, model, rental_rate):
        Vehicle.__init__(self,model, rental_rate)
    def calculate_rental(self,type2,duration):
         return self.rental_rate*duration

class Truck(Vehicle):
    def __init__(self, model, rental_rate):
        Vehicle.__init__(self,model, rental_rate)
    def calculate_rental(self,type2,duration):
        driver_allowance = 500
        print(f"\nRental amount is included the driver bata charge Rs.{driver_allowance}")
        return self.rental_rate*duration+driver_allowance

print("\n   *Welcome to Vehicle Rental System:*")

vehicle1=int(input("\nEnter needed vehicle type for rent:1.Car 2.Bike 3.Truck:"))

duration1=int(input("\nEnter duration in hours:"))

if vehicle1==1:
    ride=Car(2023,250)
    type1=int(input("1.AC 2.NONAC:"))
    print(f"\nYour rental charge is Rs.{ride.calculate_rental(type1,duration1)}")
elif vehicle1==2:
    ride=Bike(2024,100)
    print(f"\nYour rental charge is Rs.{ride.calculate_rental(1,duration1)}")
elif vehicle1==3:
    ride=Truck(2010,750)
    print(f"\nYour rental charge is Rs.{ride.calculate_rental(1,duration1)}")