from utils.screen import clear_screen
import utils.formatting as fmt
def main():
    while True:
        try:
            clear_screen()
            fmt.print_header("ChemLab Pro")
            fmt.print_menu([
                "Mole Calculator",
                "Density Calculator",
                "Temperature Converter",
                "Exit"
            ])
            choice = input("Select an option (1-4): ").strip()
            if choice == "1":
                from calculators.mole import mole_calculator
                mole_calculator()
            elif choice == "2":
                from calculators.density import density_calculator
                density_calculator()
            elif choice == "4":
                fmt.print_exit_message()
                break
            else:
                fmt.print_invalid_option_message()

        except KeyboardInterrupt:
            fmt.print_exit_message()
            break

if __name__ == "__main__":
        main()