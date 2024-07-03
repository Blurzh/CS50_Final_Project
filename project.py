# Para limpiar la pantalla
import os
# Para parar el programa
import sys
# Para cazar los grupos cuando el usuario mete las cantidades
import re
# Para dibujar las tablas
from tabulate import tabulate
# Para abrir, modificar y guardar archivos csv
import csv


def sorting_quantity(item):
        quantity = item[2]
        num, measure = quantity.split()
        num = float(num)
        if measure.lower() == "kg":
            num *= 1000
        return num

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
                ing_info[0] = input("Ingredient (Hops, Malt or Yiest): ").capitalize()
                if ing_info[0] not in possible_ing:
                    fail = True

            while not ing_info[1]:
                ing_info[1] = input("Name (variety): ").capitalize()

            fail = False  
            valid_quantity = False         
            while not valid_quantity:
                try:
                    if fail == True:
                        print("Incorrect quantity. You have to provide a number and a measure (e.g. 1 Kg, 20 g). Try again.")
                    ing_info[2] = input("Quantity (please, specify in g or kg): ").lower()
                    
                    # Me divide el input en 2 y acto seguido mira si hay errores en las entradas
                    match = re.search("^(\d*)? (g|gr|kg|Kg)?$", ing_info[2])
                    if not match:
                        raise ValueError("Incorrect quantity. You have to provide a number and a measure (e.g. 1 Kg, 20 g). Try again.")
                    if not match.group(1).isnumeric():
                        raise ValueError("Quantity must be a number.")
                    if match.group(2) not in ["g", "gr", "kg", "Kg", "KG"]:
                        raise ValueError("Invalid measure. Choose from g, gr, kg, Kg.")
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
                ing_info[3] = "After cooling the mixture"
            
            ingredients.append(ing_info)
            a = ""
            checker = input("\nDo you want to add another one? Y or N: ")
            if checker.upper() == "N":
                done = True

        # Ahora ordeno la lista de ingredientes. 1º por ingredientes, y dentro de los ingredientes, por tiempos y cantidad (en ese orden).
        ingredients.sort(key = lambda x: (x[0], x[3], sorting_quantity(x)))
        sorted_ingredients = [["Ingredient", "Variety", "Quantity", "When to be added"]]
        for _ in range(len(ingredients)):
            sorted_ingredients.append(ingredients[_])
        return sorted_ingredients
    
    
    # Imprime una tabla de los ingredientes añadidos por el usuario 
    def show_recipe(self, ing_list):
        os.system('cls||clear')
        print("--------- Brewing recipe ---------\n\n")
        print(f"For brewing a {self.name} ({self.beer_type} type of beer), you will need:\n")
        print(tabulate(ing_list, headers = "firstrow", tablefmt = "fancy_grid"))


def create_recipe_csv(beer, ingredients):
    recipe_name = beer.name + " (" + beer.beer_type + ")"
    with open(recipe_name, 'w') as new_recipe:
        writer = csv.writer(new_recipe)
        for _ in ingredients:
            writer.writerow(_)


def main():
    os.system('cls||clear')
    beer = Beer()
    users_recipe = beer.ingredients()
    # beer.show_recipe(users_recipe)
    create_recipe_csv(beer, users_recipe)

if __name__ == "__main__":
    main()





