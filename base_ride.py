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
