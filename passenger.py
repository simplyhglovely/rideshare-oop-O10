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