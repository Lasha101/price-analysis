import numpy as np

# Convert the input date into a float value
def date(date):
    try:
        date = float(date)
        date = 12 - date
        return date
    except ValueError:
        raise ValueError("Only Integer or Float!")

# Calculate the Bitcoin price at the given date using the equation
def get_value(coefs, date):
    price = np.polyval(coefs, date)
    price = round(price)
    print(f"The price on date {date} is {price}")
    return date

# Create a polynomial equation using the coefficients
def make_equation(coefs):
    equation = np.poly1d(coefs)
    return equation

# Calculate the derivative of the equation at the given value and analyze the result
def calculate_derivative(equation, value):
    derivative = np.polyder(equation)
    derivative_at_x = np.polyval(derivative, value)
    derivative_at_x = round(derivative_at_x)
    print(f"Derivative at x={value}: {derivative_at_x}")

    if derivative_at_x > 0:
        print("The derivative is positive.")
    elif derivative_at_x < 0:
        print("The derivative is negative.")
    else:
        print("The derivative is zero.")
    return round(derivative_at_x)

# Execute the main function if this file is run directly

