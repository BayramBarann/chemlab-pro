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


        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
        main()