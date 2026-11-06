from abc import ABC, abstractmethod #lab7
#lab7
class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass