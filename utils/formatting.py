def print_header(title):
    HEADER_WIDTH = 40
    print("=" * HEADER_WIDTH)
    print(title.center(HEADER_WIDTH))
    print("=" * HEADER_WIDTH)
def print_footer():
    print(f"{Color.BLUE}{'=' * 28}{Color.RESET}")
def print_result(label, value, unit):
    print(f"{label}: {value} {unit}")
def print_error(message):
    print(f"{Color.RED}Error: {message}{Color.RESET}")
def print_message(message):
    print(f"{Color.WHITE}{message}{Color.RESET}")  
def print_menu(options):
    print(Color.BLUE + "=" * 35 + Color.RESET)
    for index, option in enumerate(options, start=1):
        print(f"{Color.GREEN}{index}. {option}{Color.RESET}")
    print(Color.BLUE + "=" * 35 + Color.RESET)
def print_exit_message():
    print(f"{Color.RED}Exiting...{Color.RESET}")
def print_invalid_option_message():
    print(f"{Color.RED}Invalid option. Please select a valid number.{Color.RESET}")
def get_continue_prompt():
    while True:
        choice = input("Do you want to perform another calculation? (y/n): ").strip().lower()
        if choice in ['y', 'n']:
            return choice
        else:
            print(f"{Color.RED}Invalid option. Please enter 'y' or 'n'.{Color.RESET}")

def print_welcome_message():
    print(f"{Color.CYAN}Welcome to ChemLab Pro!{Color.RESET}")

class Color:
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    MAGENTA = "\033[95m"
    BLUE = "\033[94m"
    WHITE = "\033[97m"
    RESET = "\033[0m"

def print_banner():
    print(f"{Color.CYAN}Welcome to ChemLab Pro!{Color.RESET}")
    print(f"{Color.GREEN}Scientific Chemistry Toolkit v0.2.0.{Color.RESET}")
    print(f"{Color.YELLOW}Developed by Bayram Baran Yesil.{Color.RESET}")