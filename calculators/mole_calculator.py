from  utils.screen import clear_screen

def mole_calculator():
   
   clear_screen()
   print("=" * 10 + " Mole Calculation " + "=" * 10)

   while True:
     
     while True:
        try:
            molecular_mass = float(input(f"{'Molar Mass (g/mol)':<16}: "))
            if molecular_mass <= 0:
                print("Please insert a positive number")
                continue
            break
        except ValueError:
            print("Please insert only numbers")

     while True:
        try:
             mass = float(input(f"{'Mass (g)':<8}: "))
             if mass <= 0:
              print("Please insert a positive number")
              continue
             break
        except ValueError:
                print("Please insert only numbers")


     moles = mass / molecular_mass


     clear_screen()
     print("\n" + "=" * 28)
     print(f"{'Mass (g)':<8}: {mass:.4f}")
     print(f"{'Molar Mass (g/mol)':<8}: {molecular_mass:.4f}")
     print(f"{'Amount of Matter (mol)':<8}: {moles:.4f}")
     print("=" * 28)
     while True:
            choice = input("Do you want to continue or back to main menu? (y/n): ").strip().lower()
            if choice in ("y", "yes"):
                clear_screen()
                break
            if choice in ("n", "no"):
                clear_screen()
                return