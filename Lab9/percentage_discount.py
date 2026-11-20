from discount_strategy import DiscountStrategy


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float) -> None:
        self.percentage: float = percentage

    def apply(self, total: float) -> float: #where discount occurs if disount is applied
        return total * (1 - self.percentage / 100)