import utils.formatting as fmt
from utils.input import get_positive_float, get_choice
from utils.screen import clear_screen
import chemistry.van_der_waals_calc as vdw


def van_der_waals_calculator():
    while True:
        clear_screen()
        fmt.print_header("Van der Waals Calculator")
        fmt.print_menu([
            "Calculate Pressure",
            "Calculate Volume",
            "Calculate Temperature",
            "Calculate Moles",
            "Return to Gas Laws Menu"
        ])
        selection = get_choice("Select an option (1-5): ", ["1", "2", "3", "4", "5"])

        if selection == "5":
            return

        clear_screen()
        gases = vdw.get_available_gases()
        options = [f"{symbol} - {info['name']}" for symbol, info in gases]
        fmt.print_menu(options)
        gas_choice = get_choice("Select a gas by number: ", [str(i) for i in range(1, len(options) + 1)])

        symbol, gas_info = gases[int(gas_choice) - 1]
        a = gas_info["a"]
        b = gas_info["b"]

        try:
            if selection == "1":
                n = get_positive_float("Enter the number of moles (mol): ")
                volume = get_positive_float("Enter the volume (L): ")
                temperature = get_positive_float("Enter the temperature (K): ")
                result = vdw.calculate_pressure(n, volume, temperature, a, b)
                label, unit = "Pressure", "atm"
            elif selection == "2":
                pressure = get_positive_float("Enter the pressure (atm): ")
                n = get_positive_float("Enter the number of moles (mol): ")
                temperature = get_positive_float("Enter the temperature (K): ")
                result = vdw.calculate_volume(pressure, n, temperature, a, b)
                label, unit = "Volume", "L"
            elif selection == "3":
                pressure = get_positive_float("Enter the pressure (atm): ")
                volume = get_positive_float("Enter the volume (L): ")
                n = get_positive_float("Enter the number of moles (mol): ")
                result = vdw.calculate_temperature(pressure, volume, n, a, b)
                label, unit = "Temperature", "K"
            elif selection == "4":
                pressure = get_positive_float("Enter the pressure (atm): ")
                volume = get_positive_float("Enter the volume (L): ")
                temperature = get_positive_float("Enter the temperature (K): ")
                result = vdw.calculate_moles(pressure, volume, temperature, a, b)
                label, unit = "Moles", "mol"
        except ValueError as exc:
            fmt.print_error(str(exc))
            input("Press Enter to continue...")
            continue

        clear_screen()
        fmt.print_header("Van der Waals Results")
        fmt.print_message(f"Gas: {gas_info['name']} ({symbol})")
        fmt.print_message(f"a = {a} L^2·atm/mol^2")
        fmt.print_message(f"b = {b} L/mol")
        fmt.print_result(label, result, unit)
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
