from utils.input import get_float, get_choice
from utils.screen import clear_screen
import utils.formatting as fmt

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

CONVERSION = {
    "1": ("Celsius", "Fahrenheit", celsius_to_fahrenheit),
    "2": ("Fahrenheit", "Celsius", fahrenheit_to_celsius),
    "3": ("Celsius", "Kelvin", celsius_to_kelvin),
    "4": ("Kelvin", "Celsius", kelvin_to_celsius),
    "5": ("Fahrenheit", "Kelvin", fahrenheit_to_kelvin),
    "6": ("Kelvin", "Fahrenheit", kelvin_to_fahrenheit)
}

CONVERSION_OPTIONS = [
    "Celsius to Fahrenheit",
    "Fahrenheit to Celsius",
    "Celsius to Kelvin",
    "Kelvin to Celsius",
    "Fahrenheit to Kelvin",
    "Kelvin to Fahrenheit"
]

def temperature_calculator():
    clear_screen()
    while True:
        fmt.print_header("Temperature Converter")
        fmt.print_menu(CONVERSION_OPTIONS)
        choice = get_choice("Select a conversion option (1-6): ", CONVERSION.keys())
        from_unit, to_unit, conversion_func = CONVERSION[choice]
        value = get_float(f"Enter the temperature in {from_unit}: ")
        converted_value = conversion_func(value)
        clear_screen()
        fmt.print_header("Temperature Conversion Results")
        fmt.print_result(f"Temperature in {from_unit}", value, from_unit)
        fmt.print_result(f"Temperature in {to_unit}", converted_value, to_unit)
        fmt.print_footer()
        while True:
            continue_choice = fmt.get_continue_prompt()
            if continue_choice == 'y':
                break
            elif continue_choice == 'n':
                fmt.print_exit_message()
                return
            else:
                fmt.print_invalid_option_message()