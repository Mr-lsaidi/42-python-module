import re


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
    length = len(name)
    if length == 0:
        print('U pass and empty string in the name')
        return
    if name in cookbook.keys():
        print('The recipe "{}" already exist'.format(name))
    else:
        cookbook[name] = {
            ingredients,
            meal,
            prep_time
        }


# del_recipe("sandwich")
# get_recipe("")
add_recipe("test", ['hello'], "tfoo", "10 min")

# get_recipe("test")

# get_recipe("cake")
