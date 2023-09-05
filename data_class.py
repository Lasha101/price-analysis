import numpy as np
# Data class for encapsulating months and prices
class Data:
    def __init__(self, months, prices):
        self.months = months
        self.prices = prices

    @property
    def months(self):
        return self._months

    @months.setter
    def months(self, months):
        self._months = months

    @property
    def prices(self):
        return self._prices

    @prices.setter
    def prices(self, prices):
        self._prices = prices

    @property
    def coefs(self):
        # Calculate the regression coefficients using NumPy's polyfit function
        coefficients = np.polyfit(self.months, self.prices, deg=len(self.months) - 1)
        return coefficients