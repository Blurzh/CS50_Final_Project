# Para limpiar la pantalla
import os
# Para parar el programa
import sys
# Para cazar los grupos cuando el usuario mete las cantidades
import re
# Para ordenar la lista Ingredients bajo 2 criterios simultaneos (el tipo y el timing)
import operator
# Para dibujar las tablas
import tabulate

class Beer():
    def __init__(self, name = None, beer_type = None) -> None:
        self._name = name
        self._beer_type = beer_type
        self._ingredients = []


    def __str__(self) -> str:
        return(f"{self.name} is a {self.beer_type}")


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value


    @property
    def beer_type(self):
        return self._beer_type

    #   Tengo que hace que el tipo de birra permita espacios

    @beer_type.setter
    def beer_type(self, value):
        self._beer_type = value

    
    def ingredients(self):
        os.system('cls||clear')
        possible_ing = ["Malt", "Yiest", "Hops"]
        print("--------- Introducing ingredients ---------\n\n")
        ingredients = []
        timings = {"1. Early Boil": "First 15 minutes",
                    "2. Mid Boil": "Middle of the boil",
                    "3. Late Boil": "Last 10-15 minutes",
                    "4. Flameout": "Immediately after turning off heat",
                    "5. Whirlpool": "During cooling, while stirring",
                    "6. Dry Hopping": "During fermentation, before bottling"}
        done = False
        while not done:
            ing_info = ["", "", "", ""]
            while not self.name:
                self.name = input("Name of the beer: ").capitalize()
                right_name = re.search(f"^[a-zA-Z0-9 '-ºª]*$", self.name)
                try:
                    if not right_name:
                        raise ValueError("Invalid name. Try a different one.")
                except ValueError as e:
                    os.system('cls||clear')
                    print("--------- Introducing ingredients ---------\n\n")
                    print(e)
                    self.name = None
            

            while not self.beer_type:
                self.beer_type = input("Type of the beer: ").capitalize()
                right_name = re.search(f"^[a-zA-Z' -]*$", self.beer_type)
                try:
                    if not right_name:
                        raise ValueError("\nInvalid name. Try a different one.")
                except ValueError as e:
                    os.system('cls||clear')
                    print("--------- Introducing ingredients ---------\n\n")
                    print(f"Name of the beer: {self.name}")
                    print(e)
                    self.beer_type = None
                    
            
            
            os.system('cls||clear')
            print("--------- Introducing ingredients ---------")
            print(f"\n\nName of the beer: {self.name}")
            print(f"Type of the beer: {self.beer_type}")
            print(f"\nYou're now introducing the ingredients for brewing a {self.beer_type}, specificaly, a {self.name}. Please, follow the instructions for a clearer recipe.")
            print(f"\nYou'll be asked to introduce either {possible_ing[0]}, {possible_ing[1]}, or {possible_ing[2]}, plus their names, quantities and when they're supposed to be added.")    
            
            print("\n")
            fail = False
            while ing_info[0] not in possible_ing:
                if fail:
                    print("Please, introduce a proper ingredient from the list below.")
                ing_info[0] = input("Ingredient (Malt, Yiest or Hops): ").capitalize()
                if ing_info[0] not in possible_ing:
                    fail = True

            while not ing_info[1]:
                ing_info[1] = input("Name (variety): ").capitalize()

            fail = False  
            valid_quantity = False         
            while not valid_quantity:
                try:
                    if fail == True:
                        print("Incorrect quantity. You have to provide a number and a measure (e.g. 1 Kg, 20 g, 700 mg). Try again.")
                    ing_info[2] = input("Quantity (please, specify in mg, g or Kg): ")
                    
                    # Me divide el input en 2 y acto seguido mira si hay errores en las entradas
                    match = re.search("^(\d*)? (mg|g|gr|kg|Kg|KG)?$", ing_info[2])
                    if not match:
                        raise ValueError("Incorrect quantity. You have to provide a number and a measure (e.g. 1 Kg, 20 g, 700 mg). Try again.")
                    if not match.group(1).isnumeric():
                        raise ValueError("Quantity must be a number.")
                    if match.group(2) not in ["mg", "g", "gr", "kg", "Kg", "KG"]:
                        raise ValueError("Invalid measure. Choose from mg, g, gr, kg, Kg, KG.")
                    valid_quantity = True
                except ValueError as e:
                    print(e)
            
            if ing_info[0] == "Hops":
                print("\nWhen to add:\n")
                for _ in timings:
                    print(f"{_}: {timings[_]}")
                while not ing_info[3]:
                    choice = input("\nPlease choose an option (1-6): ")
                    if choice in ["1", "2", "3", "4", "5", "6"]:
                        ing_info[3] = list(timings.values())[int(choice) - 1]
                    else:
                        print("Please, choose an option within the given")


            if ing_info[0] == "Malt":
                print("\nWhen to add:\n1. Before boil\n2. During boil")
                while not ing_info[3]:
                    choice = input("\nPlease choose an option (1-2): ")
                    if choice in ["1", "2"]:
                        ing_info[3] = "Before boil" if choice == "1" else "During boil"
            
            if ing_info[0] == "Yiest":
                ing_info[3] == "After cooling the mixture"
            
            ingredients.append(ing_info)
            a = ""
            checker = input("\nDo you want to add another one? Y or N: ")
            if checker.upper() == "N":
                done = True

        # Ahora ordeno la lista de ingredientes. 1º por ingredientes, y dentro de los ingredientes, por tiempos y cantidad (en ese orden).
        ingredients.sort(key = operator.itemgetter(0, 3, 1))
        
        # Imprime todo seguido, incluidos los elementos vacios, en forma de lista 
        print(tabulate(ingredients, headers = ["Ingredient", "Variety", "Quantity", "When to be added"], tablefmt = "fancy_grid"))


    # def show_recipe(self, ingredients):





def main():
    os.system('cls||clear')
    beer = Beer()
    beer.ingredients()
    print(beer)
    print(beer.name)

if __name__ == "__main__":
    main()





