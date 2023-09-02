# Bitcoin Price Analysis with Regression and Derivative Calculations

In this project, I leverage programming and mathematical tools to create a continuous curve based on simulated input values. By employing regression fitting extrapolation, the program connects data points (simulated Bitcoin prices) in a way that resembles having prices available for every millisecond. The x-coordinate represents time, while the y-coordinate corresponds to the price.

## Project Overview

The primary goal of this project is to analyze Bitcoin price data and gain insights into its behavior over time. Through regression analysis, the program calculates the equation of the curve that best fits the provided data points. This equation enables us to estimate Bitcoin prices for any given date within the dataset.

## Features

- **Regression Analysis:** The program utilizes the NumPy library to perform polynomial regression fitting on the simulated Bitcoin price data. This allows us to establish a mathematical equation that approximates the relationship between time and price.

- **Extrapolation:** With the derived regression equation, the program extends the curve beyond the provided data points, enabling the estimation of Bitcoin prices at arbitrary time intervals.

- **Derivative Calculation:** The project goes beyond simple price estimation. It calculates the derivative of the curve at a specific point in time. This derivative indicates the rate of change of Bitcoin prices at that particular moment, providing insights into the price evolution.

- **Tangent Slope Analysis:** The program further interprets the derivative by calculating the inclination slope of the tangent line at the chosen time point. This slope offers an understanding of the degree of inclination of the curve at that specific moment.
- 
## Usage       !ATTANTION to the python commands! For different OS they may be different!

To utilize the Bitcoin Price Analysis program, ensure you have the following Python libraries/modules installed:

- `numpy`
- `requests`
- `pytest`

You can install these packages using the following commands:

```
pip install numpy requests pytest
```
Once you have these libraries/modules installed, you can proceed to use the program as follows:

Clone the Repository:
Clone the GitHub repository containing the Bitcoin Price Analysis project to your local machine.
```
git clone https://github.com/Lasha101/price-analysis.git
```
Navigate to the Project Directory:
Navigate to the directory where you cloned the repository.
```
cd final_project
```
Run the Program:
To use the program, execute the main script. You can do this by running the following command:
```
python project.py
```
Input a Date:
After running the script, the program will prompt you to enter a date. Please remember that the program provides simulated prices for the past 12 months. If you want to obtain the price from 3 months ago, enter 3. For a price from 5 and a half months ago, enter 5.5. The valid range for input is from 0 to 12 months. However, if you input a date outside of this range, you will still receive a price, but it will be entirely simulated. 
Observe Results:

The program will provide you with the following information in your terminal:

- Estimated Bitcoin price at the specified date.
- Derivative of the curve function at that point, indicating the rate of change of Bitcoin prices.
- Angle of inclination of the tangent line to the curve at the chosen time, offering insights into the rate of change.

Feel free to explore the code and adapt it to your specific analysis needs. 

Testing (Optional):

If you're interested in running the test suite for the program, you can do so using the pytest framework. The tests are defined in the test_project.py script. To run the tests, execute the following command:
```
pytest test_project.py
```
This will execute the test cases defined for the program functions and provide you with information about their correctness.

