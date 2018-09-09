import json
from tqdm import tqdm

outJSON = {}
outJSON["filtered_recipes"] = []

file = open("recipesjson.txt", "r")
loaded = json.loads(file.read())
RECIPES = loaded["recipes"]

VEGETARIAN = ["beef", "chicken", "pork", "fish", "cod", "tuna", "salmon", "sushi", "lamb", "duck", "turkey", "ham"
              , "pepperoni", "sausage", "bacon", "ribs", "lobster", "scallop", "shrimp", "crab", "anchovies", "crawfish"
              , "steak", "prosciutto", "filet"]

PESCETARIAN = ["beef", "chicken", "pork", "lamb", "duck", "turkey", "ham"
              , "pepperoni", "sausage", "bacon", "ribs", "lobster"
              , "steak", "prosciutto", "filet"]

DAIRY = ["cheese", "milk", "yogurt", "butter", "dairy", "cream", "leche", "mozzarella", "cheddar", "parmesan", "whey"
         "latte", "mayonnaise", "ricotta"]

GLUTEN = ["wheat", "rye", "barley", "malt", "yeast", "starch", "noodles", "pasta", "cake", "cookie", "bread", "toast"
          "pancake", "dumpling", "ramen", "flour"]

NUT = ["nut", "pine", "chesnut", "candlenut", "hazlenut", "almond", "peanut", "walnut", "macademia", "cashew", "pecan"
       , "coconut", "acorn"]

VEGAN = []
VEGAN.extend(VEGETARIAN)
VEGAN.extend(DAIRY)
VEGAN.extend(["gelatin", "honey"])


def filter_recipes(constraint):
    subset_recipes = []

    constraints = []
    if constraint == "vegetarian":
        constraints = VEGETARIAN
    elif constraint == "vegan":
        constraints = VEGAN
    elif constraint == "pescetarian":
        constraints = PESCETARIAN
    elif constraint == "nut-free":
        constraints = NUT
    elif constraint == "gluten-free":
        constraints = GLUTEN
    elif constraint == "dairy-free":
        constraints = DAIRY

    for recipe in tqdm(RECIPES, "Filtering recipes..."):
        ingredients = recipe["content"]
        found = False

        for cons in constraints:
            if cons in ingredients:
                found = True
                break

        if not found:
            subset_recipes.append(recipe)

    return subset_recipes


if __name__ == "__main__":
    constraints = ["vegetarian", "vegan", "pescetarian", "nut-free", "gluten-free", "dairy-free"]
    le_constraint_map = {}

    for constraint in tqdm(constraints, "Filtering constraints..."):
        results = filter_recipes(constraint)
        if results:
            le_constraint_map[constraint] = results

    outJSON["filtered_recipes"].append(le_constraint_map)

    with open("constrainted_recipes.json", "w") as outfile:
        json.dump(outJSON, outfile)
