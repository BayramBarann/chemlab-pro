import chemistry.gas_laws as gas_laws
import utils.formatting as fmt
from utils.input import get_positive_float, get_float, get_choice
from utils.screen import clear_screen
from chemistry.constants import R_ATM, R_JOULES, STANDARD_PRESSURE, STANDARD_TEMPERATURE
def ideal_gas_calculator():
    clear_screen()
    fmt.print_header("Ideal Gas Law Calculator")
    
    while True:
        fmt.print_menu([
            "Calculate Pressure (P)",
            "Calculate Volume (V)",
            "Calculate Temperature (T)",
            "Calculate Moles (n)",
            "Return to Gas Laws Menu"
        ])
        choice = get_choice("Select an option (1-5): ", ["1", "2", "3", "4", "5"])
        
        if choice == "1":
            V = get_positive_float("Enter the volume (in liters): ")
            n = get_positive_float("Enter the number of moles: ")
            T = get_positive_float("Enter the temperature (in Kelvin): ")
            P = gas_laws.calculate_pressure(n, V, T)
            clear_screen()
            fmt.print_header("Ideal Gas Law Results")
            fmt.print_result("Pressure (P)", P, "atm")
        elif choice == "2":
            P = get_positive_float("Enter the pressure (in atm): ")
            n = get_positive_float("Enter the number of moles: ")
            T = get_positive_float("Enter the temperature (in Kelvin): ")
            V = gas_laws.calculate_volume(n, P, T)
            clear_screen()
            fmt.print_header("Ideal Gas Law Results")
            fmt.print_result("Volume (V)", V, "L")
        elif choice == "3":
            P = get_positive_float("Enter the pressure (in atm): ")
            V = get_positive_float("Enter the volume (in liters): ")
            n = get_positive_float("Enter the number of moles: ")
            T = gas_laws.calculate_temperature(n, P, V)
            clear_screen()
            fmt.print_header("Ideal Gas Law Results")
            fmt.print_result("Temperature (T)", T, "K")
        elif choice == "4":
            P = get_positive_float("Enter the pressure (in atm): ")
            V = get_positive_float("Enter the volume (in liters): ")
            T = get_positive_float("Enter the temperature (in Kelvin): ")
            n = gas_laws.calculate_moles(P, V, T)
            clear_screen()
            fmt.print_header("Ideal Gas Law Results")
            fmt.print_result("Moles (n)", n, "mol")
        elif choice == "5":
            break
        
        while True:
            continue_choice = fmt.get_continue_prompt()
            if continue_choice == 'y':
                break
            elif continue_choice == 'n':
                fmt.print_exit_message()
                return
            else:
                fmt.print_invalid_option_message()  
            