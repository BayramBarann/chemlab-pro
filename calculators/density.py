from utils.input import get_positive_float
from utils.screen import clear_screen
import utils.formatting as fmt
def density_calculator():
    clear_screen()
    fmt.print_header("Density Calculator")
    mass = get_positive_float("Please enter the mass (in grams): ")
    volume = get_positive_float("Please enter the volume (in cubic centimeters): ")
    
    density = mass / volume
    fmt.print_footer()
    fmt.print_result("Mass", mass, "g")
    fmt.print_result("Volume", volume, "cm³")
    fmt.print_result("Density", density, "g/cm³")
    fmt.print_footer()

    while True:
        choice = fmt.get_continue_prompt()
        if choice == 'y':
            density_calculator()  # Restart the calculator
            break
        elif choice == 'n':
            fmt.print_exit_message()
            return
        else:
            fmt.print_invalid_option_message() 
