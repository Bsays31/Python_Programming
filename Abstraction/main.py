from abc import ABC , abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def types_of_vehicle(self):
        pass

    @abstractmethod
    def vehicle_lifespan(self):
        pass

    @abstractmethod
    def Purchase(self):
        pass