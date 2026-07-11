import utils.formatting as fmt
import utils.input as input_utils
from utils.screen import clear_screen

def gasmenu():
    while True:
        clear_screen()
        fmt.print_header("Gas Laws Calculator")
        fmt.print_menu([
            "Ideal Gas Law",
            "Van der Waals Equation",
            "Boyle's Law",
            "Charles's Law",
            "Avogadro's Law",
            "Return to Main Menu"
        ])
        choice = input_utils.get_choice("Select an option (1-6): ", ["1", "2", "3", "4", "5", "6"])
        
        if choice == "1":
            from calculators.gas.ideal_gas import ideal_gas_calculator
            ideal_gas_calculator()
        elif choice == "2":
            from calculators.gas.van_der_waals import van_der_waals_calculator
            van_der_waals_calculator()
        elif choice == "6":
            break