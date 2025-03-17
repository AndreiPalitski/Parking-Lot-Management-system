from datetime import datetime as dt
import csv

class Car:
    def __init__(self, car_number, phone_number, arrival_time=None):
        self.car_number = car_number
        self.phone_number = phone_number
        self.arrival_time = arrival_time or dt.now()

    def __str__(self):
        return f"Car {self.car_number} {self.phone_number} {self.arrival_time}"

    def __eq__(self, other):
        return self.car_number == other.car_number


class ParkingLot:
    def __init__(self, price_per_hour=15, maximum_capacity=10):
        self.lot = []
        self.__price_per_hour = price_per_hour
        self.__maximum_capacity = maximum_capacity

    def save_data(self):
        filename = 'Parking_Data.csv'
        header = ['car_number', 'phone_number', 'arrival_time']
        data = [[c.car_number, c.phone_number, c.arrival_time] for c in self.lot]

        with open(filename, 'w', newline="") as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(header)
            csvwriter.writerows(data)

    def get_price(self):
        return self.__price_per_hour

    def set_price(self, new_price):
        self.__price_per_hour = new_price

    def get_capacity(self):
        return self.__maximum_capacity

    def set_maximum_capacity(self, new_capacity):
        self.__maximum_capacity = new_capacity

    def add_car(self, car_number, phone_number):
        if len(self.lot) >= self.__maximum_capacity:
            print("Parking lot is full!")
            return False

        car = Car(car_number, phone_number)
        if car in self.lot:
            print("Car already in lot!")
            return False

        self.lot.append(car)
        return True

    def print_cars(self):
        print("\n### All Cars In Lot ###")
        for c in self.lot:
            print(c)

    def find_car_by_number(self, car_number):
        return next((c for c in self.lot if c.car_number == car_number), None)

    def remove_car(self, car_number):
        car = self.find_car_by_number(car_number)
        if car:
            self.lot.remove(car)
            print("Car removed successfully!")
        else:
            print("Car not found.")

    def calculate_by_car_number(self, car_number):
        car = self.find_car_by_number(car_number)
        if not car:
            print("Car not found.")
            return

        car_parking_time = self.calculate_time(car.arrival_time)
        price = self.calculate_price(car_parking_time)
        print(f"Time parked: {car_parking_time:.2f} hours")
        print(f"Total price: ${price:.2f}")

    def calculate_time(self, start_time: dt) -> float:
        return (dt.now() - start_time).total_seconds() / 3600

    def calculate_price(self, hours: float):
        return hours * self.__price_per_hour

    def clear_parking(self):
        self.lot.clear()

    def show_how_many_parked_more_than_24_hours(self):
        count = sum(1 for c in self.lot if self.calculate_time(c.arrival_time) > 24)
        print(f"Cars parked more than 24 hours: {count}")


def get_car_details_from_user(parking):
    car_number = input("Enter car number: ")
    phone_number = input("Enter phone number: ")
    if parking.add_car(car_number, phone_number):
        print("Car added successfully!")


def get_car_to_remove(parking):
    car_number = input("Enter car number to remove: ")
    parking.remove_car(car_number)


def admin_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin" and password == "admin":
        print("Welcome, Admin!")
        main_admin()
    else:
        print("Incorrect credentials.")
        menu()


def main_admin():
    parking_lot = ParkingLot()

    while True:
        print("\n### Admin Menu ###")
        print("[1] Change price per hour")
        print("[2] Change maximum capacity")
        print("[3] Clear parking lot")
        print("[4] Show all parked cars")
        print("[5] Show cars parked over 24 hours")
        print("[0] Exit")

        action = input("Option: ")

        if action == "1":
            new_price = float(input("Enter new price per hour: "))
            parking_lot.set_price(new_price)
            print("Price updated!")

        elif action == "2":
            new_capacity = int(input("Enter new maximum capacity: "))
            parking_lot.set_maximum_capacity(new_capacity)
            print("Capacity updated!")

        elif action == "3":
            parking_lot.clear_parking()
            print("Parking lot cleared!")

        elif action == "4":
            parking_lot.print_cars()

        elif action == "5":
            parking_lot.show_how_many_parked_more_than_24_hours()

        elif action == "0":
            print("Exiting Admin Menu...")
            break

        else:
            print("Invalid option, try again.")


def menu():
    parking_lot = ParkingLot()

    while True:
        print("\n### Parking Lot Menu ###")
        print("[1] Enter a car")
        print("[2] Remove a car")
        print("[3] Show parking price")
        print("[4] Admin Panel")
        print("[0] Exit")

        option = input("Enter your option: ")

        if option == "1":
            get_car_details_from_user(parking_lot)

        elif option == "2":
            get_car_to_remove(parking_lot)

        elif option == "3":
            print(f"Parking price per hour: ${parking_lot.get_price()}")

        elif option == "4":
            admin_user()

        elif option == "0":
            print("Thank you! Goodbye!")
            break

        else:
            print("Invalid option, please try again.")


# Start the program
menu()
