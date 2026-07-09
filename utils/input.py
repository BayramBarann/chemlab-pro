def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please insert a positive number")
                continue
            return value
        except ValueError:
            print("Please insert only numbers")
def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please insert only numbers")
def get_choice(prompt, choices):
    while True:
        choice = input(prompt).strip()
        if choice in choices:
            return choice
        else:
            print(f"Invalid option. Please select from {', '.join(choices)}.")
