import chemistry.gas_laws as gas_laws
import utils.formatting as fmt
from utils.input import get_positive_float, get_float, get_choice
from utils.screen import clear_screen

def ideal_gas_calculator():
    clear_screen()
    while True:
        fmt.print_header("Ideal Gas Law Calculator")
        fmt.print_menu([
            "Calculate Pressure (P)",
            "Calculate Volume (V)",
            "Calculate Temperature (T)",
            "Exit"
        ])
        choice = get_choice("Select an option (1-4): ", ["1", "2", "3", "4"])
        if choice == "1":
            n = get_positive_float("Enter the number of moles (n): ")
            T = get_positive_float("Enter the temperature (T) in Kelvin: ")
            V = get_positive_float("Enter the volume (V) in liters: ")
            P = gas_laws.calculate_pressure(n, T, V)
            clear_screen()
            fmt.print_header("Ideal Gas Law Results")
            fmt.print_result("Pressure (P)", P, "atm")
        elif choice == "2":
            n = get_positive_float("Enter the number of moles (n): ")
            T = get_positive_float("Enter the temperature (T) in Kelvin: ")
            P = get_positive_float("Enter the pressure (P) in atm: ")
            V = gas_laws.calculate_volume(n, T, P)
            clear_screen()
            fmt.print_header("Ideal Gas Law Results")
            fmt.print_result("Volume (V)", V, "L")
        elif choice == "3":
            n = get_positive_float("Enter the number of moles (n): ")
            P = get_positive_float("Enter the pressure (P) in atm: ")
            V = get_positive_float("Enter the volume (V) in liters: ")
            T = gas_laws.calculate_temperature(n, P, V)
            clear_screen()
            fmt.print_header("Ideal Gas Law Results")
            fmt.print_result("Temperature (T)", T, "K")
        elif choice == "4":
            fmt.print_exit_message()
            break
        else:
            fmt.print_invalid_option_message()

        while True:
            continue_choice = fmt.get_continue_prompt()
            if continue_choice == 'y':
                break
            elif continue_choice == 'n':
                fmt.print_exit_message()
                return