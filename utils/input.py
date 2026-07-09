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