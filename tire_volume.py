# Import the date and math tools.
from datetime import date
import math

# Get today's date.
today = date.today()

# Ask the user to enter tire measurements.
width = int(input("Enter the width of the tire in mm: "))
aspect_ratio = int(input("Enter the aspect ratio of the tire: "))
diameter = int(input("Enter the diameter of the wheel in inches: "))

# Calculate the approximate volume of the tire in liters.
part = width * aspect_ratio + 2540 * diameter
volume = math.pi * width ** 2 * aspect_ratio * part / 10000000000

print(f"The approximate volume is {volume:.2f} liters")

# Extra feature: estimate the cost of four tires.
answer = input(
    "Would you like to estimate the cost of four tires? (yes/no): "
)

if answer.lower() == "yes":
    # Ask for the price of one tire.
    price = float(input("Enter the price of one tire: "))

    # Calculate the total cost of four tires.
    total_price = price * 4

    # Display the total cost.
    print(f"The cost of four tires is ${total_price:.2f}")
    
# Save the tire measurements, volume, and date to a file.
# Append mode keeps previous records.
with open("volumes.txt", "a") as file:
    file.write(
        f"{today}, {width}, {aspect_ratio}, "
        f"{diameter}, {volume:.2f}\n"
    )
