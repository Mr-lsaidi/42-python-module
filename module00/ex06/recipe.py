import sys

cookbook = {
    "sandwich": {
        "ingredients": ["ham", "bread" "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": "10 minutes"
    },
    "cake": {
        "ingredients": ["flour", "sugar" "eggs"],
        "meal": "dessert",
        "prep_time": "60 minutes"
    },
    "salad": {
        "ingredients": ["avocado", "arugula" "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": "15 minutes"
    }
}


def get_recipe(name):
    length = len(name)
    if length == 0:
        print('U pass and empty string in the name')
        return
    if name in cookbook.keys():
        print('Recipe for {}:'.format(name))
        print('Ingredients list: {}'.format(cookbook[name]['ingredients']))
        print('To be eaten for {}.'.format(cookbook[name]['meal']))
        print('Takes {} of cooking.'.format(cookbook[name]['prep_time']))
    else:
        print('there is no recipe with the name {}'.format(name))


def del_recipe(name):
    length = len(name)
    if length == 0:
        print('U pass and empty string in the name')
        return
    if name in cookbook.keys():
        del cookbook[name]
    else:
        print('there is no recipe with the name {}'.format(name))


def add_recipe(name, ingredients, meal, prep_time):
    try:
        # check ingredients
        i = 0
        if not ingredients or isinstance(ingredients, list) == False:
            raise ValueError("Error in the ingredients")
        for ing in ingredients:
            i += 1
            if len(ing.strip()) == 0:
                raise ValueError(
                    "U pass an empty ingredient index {}".format(i))
        # check name
        if not name or isinstance(name, str) == False:
            raise ValueError("Error in the name")
        # check meal
        if not meal or isinstance(meal, str) == False:
            raise ValueError("Error in the meal")
        # check prep_time
        if not prep_time or isinstance(prep_time, str) == False:
            raise ValueError("Error in the prep_time")

        if name in cookbook.keys():
            raise ValueError('The recipe "{}" already exist'.format(name))
        else:
            cookbook[name] = {
                "ingredients": ingredients,
                "meal": meal,
                "prep_time": prep_time
            }
    except Exception as e:
        print(e)


def print_recipes():
    for name in cookbook.keys():
        print('{}'.format(name))


def recipe():
    option = 0
    while not option == 5:  
        print("Please select an option by typing the corresponding number:")
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the cookbook")
        print("5: Quit")
        print(">> ", end="")
        sys.stdout.flush()
        try:
            option = int(sys.stdin.readline())
        except ValueError:
            option = 0
        if option == 1:
            name = input("Enter the name of the recipe you'd like to add: ")
            ingredients = input("Enter the ingredients in the format "
                                "'bread,butter,jam...': ").split(',')
            meal = input("Enter the type of meal (lunch, dessert...): ")
            prep_time = input("Enter the recipe's prep time, in minutes: ")

            add_recipe(name, ingredients, meal, prep_time)
        elif option == 2:
            name = input("Enter the name of the recipe you'd like to delete: ")
            del_recipe(name)
        elif option == 3:
            name = input("Enter the name of the recipe you'd like to print: ")
            get_recipe(name)
        elif option == 4: 
            print_recipes()
        elif option == 5:
            print("Cookbook closed.")
        else:
            print ('This option does not exist, please type the corresponding number.\nTo exit, enter 5.')

recipe()
