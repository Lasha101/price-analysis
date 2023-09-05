import matplotlib.pyplot as plt
import numpy as np

def plot_curve(coefs):
    x = np.linspace(1, 12, 1000)  # Create an array of x values
    y = np.polyval(coefs, x)  # Calculate y values using the coefficients

    plt.figure(figsize=(8, 6))  # Create a new figure
    plt.plot(x, y, label='Bitcoin Price Curve', color='blue')
    plt.xlabel('Months')
    plt.ylabel('Price')
    plt.title('Bitcoin Price Curve')
    plt.grid(True)
    plt.legend()
    plt.show()

# Execute the main function if this file is run directly
