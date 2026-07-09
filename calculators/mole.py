from utils.input import get_positive_float
from utils.screen import clear_screen
import utils.formatting as fmt
def mole_calculator():
   
   clear_screen()
   

   while True:
     
     mass = get_positive_float("Enter the mass of the substance (in grams): ")
     molecular_mass = get_positive_float("Enter the molar mass of the substance (in g/mol): ")
     moles = mass / molecular_mass
     clear_screen()
     fmt.print_footer()
     fmt.print_result("Mass (g)", mass, "g")
     fmt.print_result("Molar Mass (g/mol)", molecular_mass, "g/mol")
     fmt.print_result("Amount of Matter (mol)", moles, "mol")
     fmt.print_footer()
     while True:
            choice = fmt.get_continue_prompt()
            if choice in ("y", "yes"):
                clear_screen()
                break
            if choice in ("n", "no"):
                clear_screen()
                return