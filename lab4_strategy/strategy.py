from abc import ABC, abstractmethod


class DeliveryContext:
    def __init__(self):
        self.delivery_strategy = None

    def set_delivery_strategy(self, delivery_strategy):
        self.delivery_strategy = delivery_strategy

    def calculate_delivery_cost(self, order):
        if self.delivery_strategy is not None:
            return self.delivery_strategy.calculate_delivery_cost(order)
        else:
            raise ValueError("Delivery strategy is not set")


class DeliveryStrategy(ABC):
    @abstractmethod
    def calculate_delivery_cost(self, order):
        pass


class SelfPickupStrategy(DeliveryStrategy):
    def calculate_delivery_cost(self, order):
        """Calculation of the cost of delivery for pickup"""
        return 0


class ExternalDeliveryStrategy(DeliveryStrategy):
    def calculate_delivery_cost(self, order):
        """Calculation of the cost of delivery by an external delivery service"""
        return "External delivery cost"


class InternalDeliveryStrategy(DeliveryStrategy):
    def calculate_delivery_cost(self, order):
        """Calculation of the cost of delivery by our own delivery service"""
        return "Internal delivery cost"
