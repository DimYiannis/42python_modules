
def validate_ingredients(ingredients: str) -> str:
    """
    validate a spells ingredients
    returns a str with valid or invalid
    used set to exclude duplicates
    """
    okay = {"fire", "water", "earth", "air"}

    ingredient_set = set()
    for item in ingredients.split():
        ingredient_set.add(item.strip())


    if any(ingredient in okay for ingredient in  ingredient_set):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"


