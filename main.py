from utils.screen import clear_screen
def main():
    while True:
        try:
            clear_screen()
            print("=" * 35)
            print("        ChemLab Pro")
            print("=" * 35)
            print("1. Mole Calculator")
            print("2. Density Calculator")
            print("3. Temperature Converter")
            print("4. Exit")
            choice = input("Select an option (1-4): ").strip()
            if choice == "1":
                from calculators.mole_calculator import mole_calculator
                mole_calculator()
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid option. Please select a number between 1 and 4.")

        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
        main()