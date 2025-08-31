"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients`.

    :param dish_name: str - containing the dish name.
    :param dish_ingredients: list - dish ingredients.
    :return: tuple - containing (dish_name, ingredient set).

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """

    pass


def check_drinks(drink_name, drink_ingredients):
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name`, based on `drink_ingredients`.

    :param drink_name: str - name of the drink.
    :param drink_ingredients: list - ingredients in the drink.
    :return: str - drink_name appended with "Mocktail" or "Cocktail".

    The function should return the name of the drink followed by "Mocktail" (non-alcoholic) and drink
    name followed by "Cocktail" (includes alcohol).

    """

    pass


def categorize_dish(dish_name, dish_ingredients):
    """Categorize `dish_name` based on `dish_ingredients`.

    :param dish_name: str - dish to be categorized.
    :param dish_ingredients: set - ingredients for the dish.
    :return: str - the dish name appended with ": <CATEGORY>".

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    `<CATEGORY>` can be any one of  (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`

    Using concept: loops to iterate through the available meal categories might be useful here.
    If all the elements of <set_1> are contained within <set_2>, then <set_1> <= <set_2>.
    The method equivalent of <= is <set>.issubset(<iterable>)
    concept: tuples can contain any data type, including other tuples. Tuples can be formed using (<element_1>, <element_2>) or via the tuple() constructor.
    Elements within concept: tuples can be accessed from the left using a 0-based index number, or from the right using a -1-based index number.
    The set() constructor can take any iterable as an argument. concept: lists are iterable.
    concept: strings can be concatenated with the + sign.
    """
    # Store category names along with their sets
    categories = {
        "VEGAN": VEGAN,
        "VEGETARIAN": VEGETARIAN,
        "PALEO": PALEO,
        "KETO": KETO,
        "OMNIVORE": OMNIVORE
    }
    # Check which category the dish ingredients belong to
    for category_name, category_set in categories.items():
        if dish_ingredients.issubset(category_set):
            return f"{dish_name}: {category_name}"

    return f"{dish_name}: UNKNOWN"



# print(categorize_dish('Shrimp Bacon and Crispy Chickpea Tacos with Salsa de Guacamole', {'shrimp', 'bacon', 'avocado', 'chickpeas',
#                                                                                          'fresh tortillas', 'sea salt', 'guajillo chile', 'slivered almonds', 'olive oil', 'butter', 'black pepper', 'garlic', 'onion'}))

def tag_special_ingredients(dish):
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`.

    :param dish: tuple - of (dish name, list of dish ingredients).
    :return: tuple - containing (dish name, dish special ingredients).

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.

    identify the elements that are present in the dish ingredients and in the special_ingredients constant
    We can call it as intersection.
    """
    dish_name = dish[0]
    dish_ingredients = dish[1]
    print(dish_ingredients)

    return (dish_name, set(dish_ingredients) & SPECIAL_INGREDIENTS)
# print( tag_special_ingredients(('Ginger Glazed Tofu Cutlets', ['tofu', 'soy sauce', 'ginger', 'corn starch', 'garlic', 'brown sugar', 'sesame seeds', 'lemon juice'])))



def compile_ingredients(dishes):
    """Create a master list of ingredients.

    :param dishes: list - of dish ingredient sets.
    :return: set - of ingredients compiled from `dishes`.

    This function should return a `set` of all ingredients from all listed dishes.

    list of sets to a set
    using union function
    """

    empty = set()
    for dish in dishes:
       empty = dish | empty
    return empty
dishes = [ {'tofu', 'soy sauce', 'ginger', 'corn starch', 'garlic', 'brown sugar', 'sesame seeds', 'lemon juice'},
           {'pork tenderloin', 'arugula', 'pears', 'blue cheese', 'pine nuts',
           'balsamic vinegar', 'onions', 'black pepper'},
           {'honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber'}]
# print(compile_ingredients(dishes))



def separate_appetizers(dishes, appetizers):
    """Determine which `dishes` are designated `appetizers` and remove them.

    :param dishes: list - of dish names.
    :param appetizers: list - of appetizer names.
    :return: list - of dish names that do not appear on appetizer list.

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """

    return set(dishes) - set(appetizers)


dishes = ['Avocado Deviled Eggs', 'Flank Steak with Chimichurri and Asparagus', 'Kingfish Lettuce Cups',
          'Grilled Flank Steak with Caesar Salad', 'Vegetarian Khoresh Bademjan', 'Avocado Deviled Eggs',
          'Barley Risotto', 'Kingfish Lettuce Cups']

appetizers = ['Kingfish Lettuce Cups', 'Avocado Deviled Eggs', 'Satay Steak Skewers',
              'Dahi Puri with Black Chickpeas', 'Avocado Deviled Eggs', 'Asparagus Puffs',
              'Asparagus Puffs']

# print(separate_appetizers(dishes, appetizers))

def singleton_ingredients(dishes, intersection):
    """Determine which `dishes` have a singleton ingredient (an ingredient that only appears once across dishes).

    :param dishes: list - of ingredient sets.
    :param intersection: constant - can be one of `<CATEGORY>_INTERSECTIONS` constants imported from `sets_categories_data.py`.
    :return: set - containing singleton ingredients.

    Each dish is represented by a `set` of its ingredients.

    Each `<CATEGORY>_INTERSECTIONS` is an `intersection` of all dishes in the category. `<CATEGORY>` can be any one of:
        (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).

    The function should return a `set` of ingredients that only appear in a single dish.
    """
    empty = set()
    for dish in dishes:
        empty = dish ^ empty
    return empty - intersection


dishes = [ {'tofu', 'soy sauce', 'ginger', 'corn starch', 'garlic', 'brown sugar', 'sesame seeds', 'lemon juice'},
           {'pork tenderloin', 'arugula', 'pears', 'blue cheese', 'pine nuts',
           'balsamic vinegar', 'onions', 'black pepper'},
           {'honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber'},
           ]

VEGAN_INTERSECTIONS = {'brown sugar', 'carrot', 'sugar', 'vegetable stock', 'fresh ginger', 'nutritional yeast',
                      'cayenne pepper', 'olive oil', 'lemon', 'ginger', 'red onion', 'pomegranate molasses',
                      'onion', 'water', 'chickpea flour', 'orange zest', 'coconut oil', 'smoked paprika',
                      'lemon zest', 'sunflower oil', 'orange juice', 'black pepper', 'cinnamon powder',
                      'mushrooms', 'cloves', 'salt', 'oil', 'vegan butter', 'turmeric', 'tomato paste',
                      'mustard seeds', 'bell pepper', 'rosemary', 'vinegar', 'tomatoes', 'flour', 'soy sauce',
                      'lemon juice', 'garlic'}

print(singleton_ingredients(dishes, VEGAN_INTERSECTIONS))