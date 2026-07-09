def print_header(title):
    HEADER_WIDTH = 40
    print("=" * HEADER_WIDTH)
    print(title.center(HEADER_WIDTH))
    print("=" * HEADER_WIDTH)
def print_footer():
    print("=" * 28)
def print_result(label, value, unit):
    print(f"{label:<8}: {value:.4f} {unit}")
def print_error(message):
    print(f"Error: {message}")
def print_message(message):
    print(message) 
def print_menu(options):
    print("=" * 35)
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")
    print("=" * 35)
def print_exit_message():
    print("Exiting...")
def print_invalid_option_message():
    print("Invalid option. Please select a valid number.")
def get_continue_prompt():
    while True:
        choice = input("Do you want to perform another calculation? (y/n): ").strip().lower()
        if choice in ['y', 'n']:
            return choice
        else:
            print("Invalid option. Please enter 'y' or 'n'.")
    
def print_welcome_message():
    print("Welcome to ChemLab Pro!")