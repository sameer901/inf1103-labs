from discount_strategy import DiscountStrategy


class NoDiscount(DiscountStrategy): #Default strategy if no discount applied
    def apply(self, total: float) -> float:
        return total