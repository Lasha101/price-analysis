import numpy as np

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