
import random
import requests
import sys
import numpy as np

# The main entry point of the program
def main():
    years = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    prices = get_bitcoin_prices()

    # Create a Data object with years and prices
    data = Data(years, prices)
    coefs = data.coefs
    make_equation(coefs)

    # Get user input for a specific date
    date1 = input("Date: ")
    time = date(date1)

    # Get the value of Bitcoin price at the given date
    value = get_value(coefs, time)
    equation = make_equation(coefs)

    # Calculate the derivative of the equation and analyze the results
    derivative = calculate_derivative(equation, value)
    inclination_slope(derivative)

# Data class for encapsulating years and prices
class Data:
    def __init__(self, years, prices):
        self.years = years
        self.prices = prices

    @property
    def years(self):
        return self._years

    @years.setter
    def years(self, years):
        self._years = years

    @property
    def prices(self):
        return self._prices

    @prices.setter
    def prices(self, prices):
        self._prices = prices

    @property
    def coefs(self):
        # Calculate the regression coefficients using NumPy's polyfit function
        coefficients = np.polyfit(self.years, self.prices, deg=len(self.years) - 1)
        return coefficients

# Retrieve Bitcoin prices from the CoinDesk API and generate random fluctuations
def get_bitcoin_prices():
    prices = []
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    try:
        response = requests.get(url)
        data = response.json()
        string_price = float(data['bpi']['USD']['rate_float'])
        price = string_price
        price = price / 1000

        # Generate random fluctuations for 10 iterations
        for _ in range(10):
            price = round(price * random.uniform(0.1, 2))
            prices.append(price)
    except requests.RequestException:
        sys.exit()

    print()
    print(prices)
    return prices

# Convert the input date into a float value
def date(date):
    try:
        date = float(date)
        return date
    except ValueError:
        raise ValueError("Only Integer or Float!")

# Calculate the Bitcoin price at the given date using the equation
def get_value(coefs, date):
    price = np.polyval(coefs, date)
    print(f"The price on date {date} is {price}")
    return date

# Create a polynomial equation using the coefficients
def make_equation(coefs):
    equation = np.poly1d(coefs)
    return equation

# Calculate the derivative of the equation at the given value and analyze the result
def calculate_derivative(equation, value):
    derivative = np.polyder(equation)
    print("DERIVATIVE -----", str(derivative))
    derivative_at_x = np.polyval(derivative, value)
    print("VALUE -----: ", str(value))
    print(f"Derivative at x={value}: {derivative_at_x}")

    if derivative_at_x > 0:
        print("The derivative is positive.")
    elif derivative_at_x < 0:
        print("The derivative is negative.")
    else:
        print("The derivative is zero.")
    return round(derivative_at_x)

# Calculate the inclination slope at the given x value
def inclination_slope(x):
    angle_radians = np.arctan(x)
    angle_degrees = np.degrees(angle_radians)

    if angle_degrees < 0:
        angle_degrees += 180
        if angle_degrees > 90:
            angle_degrees = (180 - angle_degrees) * -1
    angle_degrees = round(angle_degrees)
    print(f"The angle of inclination at x={x} is {angle_degrees} degrees.")
    return angle_degrees

# Execute the main function if this file is run directly
if __name__ == "__main__":
    main()

