from utils.input import get_positive_float
def density_calculator():
    print("Welcome to the Density Calculator!")
    mass = get_positive_float("Please enter the mass (in grams): ")
    volume = get_positive_float("Please enter the volume (in cubic centimeters): ")
    
    density = mass / volume
    print(f"The density is: {density} g/cm³")