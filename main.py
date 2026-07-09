from utils.screen import clear_screen
import utils.formatting as fmt
def main():
    while True:
        try:
            clear_screen()
            fmt.print_banner()
            fmt.print_menu([
                "Mole Calculator",
                "Density Calculator",
                "Temperature Converter",
                "Gas Laws",
                "Exit"
            ])
            choice = input("Select an option (1-5): ").strip()
            if choice == "1":
                from calculators.mole import mole_calculator
                mole_calculator()
            elif choice == "2":
                from calculators.density import density_calculator
                density_calculator()
            elif choice == "3":
                from calculators.temperature import temperature_calculator
                temperature_calculator()
            elif choice == "5":
                fmt.print_exit_message()
                break

            elif choice == "4":
                from calculators.gas.gasmenu import gasmenu
                gasmenu()
            else:
                fmt.print_invalid_option_message()

        except KeyboardInterrupt:
            fmt.print_exit_message()
            break

if __name__ == "__main__":
        main()