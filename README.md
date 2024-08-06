Here we have a basic beer recipe's book.

When we enter the program we'll see the menu with all the option the user can go through.

Option 1: Create a recipe.
    Here a Beer() instance will be created.
    The user is prompted for a name, a beer type and will get into a loop where a list of ingredients will be loaded. Name have absolute freedom, while 'Ingredient, 'Quantity' and 
    'When to be added' have to follow specific easy rules given when entering them. After entering all information about one ingredient, the user will be asked if the loop should be
    repeated for adding another ingredient for the recipe or stop it and get back to the menu.

Option 2: Save recipe.
    The recipe introduced in Option 1 will be saved in a text file with name "Name (Type).csv". If the user didn't entered any recipe with Option 1, an error message will be prompted allowing the user to know the impossibility to save something that doesn't exist.
    If we enter 2 recipes, one after the other, only the last one will be saved this way.
    
Option 3: See existing recipes:
    The program will access the directory where the file is located, check and print the name of all '.csv' files (it will show any '.csv' files in the directory, so it's recommended to only store beer recipes in here).

Option 4: See recipe's ingredients
    First, it will access to all the '.csv' files in the directory where the program file is located, then will display all the recipes (suposing there're recipes in the folder) and expect the user to enter which recipe wants to see.
    When the option is entered, the program opens the file related to it and displays it in a table format, so the information saved in 'Option 2' can be followed. 

Option 0:
    Exits the program.
