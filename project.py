from prices import date, bitcoin_prices
from data_class import Data
from math_tools import make_equation, get_value, calculate_derivative
from angle import inclination_slope
from visualizing import plot_curve

# The main entry point of the program
def main():
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    prices = bitcoin_prices()

    # Create a Data object with years and prices
    data = Data(months, prices)
    coefs = data.coefs
    make_equation(coefs)

    # Get user input for a specific date
    user_input = input("Date: ")
    time = date(user_input)

    # Get the value of Bitcoin price at the given date
    value = get_value(coefs, time)
    equation = make_equation(coefs)

    # Calculate the derivative of the equation and analyze the results
    derivative = calculate_derivative(equation, value)
    inclination_slope(derivative)

    plot_curve(coefs)



# Execute the main function if this file is run directly
if __name__ == "__main__":
    main()

