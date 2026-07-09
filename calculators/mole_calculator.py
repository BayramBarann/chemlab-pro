from utils.input import get_positive_float
from utils.screen import clear_screen

def mole_calculator():
   
   clear_screen()
   print("=" * 10 + " Mole Calculation " + "=" * 10)

   while True:
     
     mass = get_positive_float("Enter the mass of the substance (in grams): ")
     molecular_mass = get_positive_float("Enter the molar mass of the substance (in g/mol): ")
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