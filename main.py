from abc import ABC, abstractmethod


class Ride(ABC):
    def __init__(self, distance_km: float):
        self.distance_km = distance_km
        self.is_completed = False


    @abstractmethod
    def calculate_fare(self):
        pass


    @abstractmethod
    def start_ride(self):
        pass

    @abstractmethod
    def complete_ride(self):
        pass

class PassengerAccount:

    def __init__(self, name):
        self.name = name
        self.__wallet_balance = 0.0

    def top_up_wallet(self, amount):
        if amount < 0:
            raise ValueError("Top-up amount cannot be negative!")

        self.__wallet_balance += amount

        print(f"Successfully added Php {amount:.2f}")
        print(f"Current balance: Php {self.__wallet_balance:.2f}")

    def pay_for_ride(self, fare_amount):
        if self.__wallet_balance < fare_amount:
            raise ValueError("Insufficient funds! Please top up.")

        self.__wallet_balance -= fare_amount

        print(f"Payment successful: Php {fare_amount:.2f}")
        print(f"Remaining balance: Php {self.__wallet_balance:.2f}")

class DriverAccount:
    def __init__(self, name, vehicle_plate):
        self.name = name
        self.vehicle_plate = vehicle_plate
        self.__rating = 5.0
        self.__total_trips = 0


    def add_rating(self, new_rating):
        if new_rating < 1.0 or new_rating > 5.0:
            raise ValueError("Invalid rating!")
        total_score = (self.__rating * self.__total_trips) + new_rating
        self.__total_trips += 1
        self.__rating = total_score / self.__total_trips


    def get_rating_info(self):
        return f"Driver {self.name} ({self.vehicle_plate}) - Rating: {self.__rating:.2f} stars ({self.__total_trips} trips)"

