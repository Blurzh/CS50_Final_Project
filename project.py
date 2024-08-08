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





# Implementar inputs de name y beer_type al comienzo de la clase y liberar el inicio del metodo ingredients





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

    
    # Revisar el metodo. Han salido ya 2 recetas con espacios en blanco que afean la tabla de la Option 4 a topew

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
                right_name = re.search(r"^[a-zA-Z0-9 '-ºª]*$", self.name)
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
                right_name = re.search(r"^[a-zA-Z' -]*$", self.beer_type)
                try:
                    if not right_name:
                        raise ValueError("\nInvalid name. Try a different one.")
                except ValueError as e:
                    os.system('cls||clear')
                    print("--------- Introducing ingredients ---------\n\n")
                    print(f"Name of the beer: {self.name}\n")
                    print(e)
                    self.beer_type = None

            
            os.system('cls||clear')
            print("--------- Introducing ingredients ---------")
            print(f"\n\nName of the beer: {self.name}")
            print(f"Type of the beer: {self.beer_type}")
            print(f"\nYou're now introducing the ingredients for brewing a {self.beer_type}, specificaly, a {self.name}. Please, follow the instructions for a clearer recipe.")
            print(f"\nYou'll be asked to introduce either {possible_ing[0]}, {possible_ing[1]}, or {possible_ing[2]}, plus their names, quantities and when they're supposed to be added.\n")    

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
                    
                    match = re.search(r"^(\d*.?\d*?) (g|gr|kg)$", ing_info[2])
                    if not match:
                        raise ValueError("Incorrect quantity. You have to provide a number and a measure (e.g. 1 kg, 20 g). Try again.")
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
            # a = ""
            checker = input("\nDo you want to add another one? Y or N: ")
            if checker.upper() == "N":
                done = True

        # Ahora ordeno la lista de ingredientes. 1º por ingredientes, y dentro de los ingredientes, por tiempos y cantidad (en ese orden).
        ingredients.sort(key = lambda x: (x[0], x[3], sorting_quantity(x)))
        sorted_ingredients = [["Ingredient", "Variety", "Quantity", "When to be added"]]
        for _ in range(len(ingredients)):
            sorted_ingredients.append(ingredients[_])
        return sorted_ingredients


def sorting_quantity(item):
        quantity = item[2]
        num, measure = quantity.split()
        num = float(num)
        if measure.lower() == "kg":
            num *= 1000
        return num


def show_recipe(ingredients, name_and_type):
    os.system('cls||clear')
    name, beer_type = name_and_type[:-5].split(sep=' (')
    print("--------- Brewing recipe ---------\n\n")
    print(f"For brewing a {name} ({beer_type} type of beer), you will need:\n")
    print(tabulate(ingredients, headers = "firstrow", tablefmt = "fancy_grid"))
    refresh_screen = input("\n\nEnter any key to close this recipe: ")


# Tengo que tener cuidado con esta funcion. Recibe una beer con nombre y tipo, y con ello tiene que hacer un .csv
def save_recipe_csv(beer, list_to_save):
    try:
        recipe_name = beer.name + " (" + beer.beer_type + ").csv"
    except TypeError:
        return "\nImpossible to create the recipe, since none was entered. If you want to save one, please, select option '1.- Create Recipe'"
    with open(recipe_name, 'w', newline='') as new_recipe:
        writer = csv.writer(new_recipe)
        for _ in list_to_save:
            writer.writerow(_)


def open_recipe(option):
    with open(option) as file:
        recipe_to_open = file.readlines()
    aux_dict = []
    for _ in range(len(recipe_to_open)):
        aux_dict.append(recipe_to_open[_].split(sep=','))
    return aux_dict


# Esta función va a ser problematica ya que tiene el path de mi carpeta del pc, no la del repositorio de GitHub en si
def show_all_csv_available():
    os.system('cls||clear')
    current_directory = os.path.dirname(os.path.abspath(__file__))
    all_files = os.listdir(current_directory)    
    csv_files = list(filter(lambda f: f.endswith('.csv'), all_files))
    print("Existing recipes:\n")
    for _ in range(len(csv_files)):
        print(f"{_+1}.- {csv_files[_][:-4]}")
    return csv_files


def choosing_recipe():
    csv_files = show_all_csv_available()
    option = input("\nWhich beer would you like to check? ")
    try:
        option = csv_files[int(option)-1]
    except IndexError:
        option = "That's not an available recipe. Please, select a new option\n\n"
    return option


# Esta función necesita ser pulida mucho mucho mas
def menu():
    option = -1
    fail = ""
    while option != "0":
        os.system('cls||clear')
        # Puedes hacer un menu mas bonito con Tabulate (no sé, piénsalo)

        # Cuando printea algo y vuelve al menu borra lo que ha escrito. Hay que solucionar eso

        option = input("--------- Menu ---------\n\nOptions:\n\n1.- Create recipe\n2.- Save Recipe\n3.- See existing recipes\n4.- See recipe's ingredients\n0.- Exit program\n\n" + fail +"\n\nOption: ")
        fail = ""
        if option == "1":
            beer = Beer()
            list_to_save = beer.ingredients()
        elif option == "2":
            try:
                for _ in list_to_save:
                    print(_)
                save_recipe_csv(beer, list_to_save)
            except:
                fail = "Impossible to create the recipe, since none was entered. If you want to save one, please, select option '1.- Create Recipe'\n\n"
        elif option == "3":
            show_all_csv_available()
            refresh_screen = input("\n\nEnter any key to get back to the menu: ")
        elif option == "4":
            name = choosing_recipe()
            if name == "That's not an available recipe. Please, select a new option\n\n":
                fail = name
            else:
                ingredients = open_recipe(name)
                show_recipe(ingredients, name)
        else:
            fail = "That option doesn't exists. Please, select one shown above."


def main():
    os.system('cls||clear')
    menu()

if __name__ == "__main__":
    main()





