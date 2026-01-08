

def record_spell(spell_name: str, ingredients: str) -> str:
    """
    validate a spell's ingredients and record if its valid
    it performs a late import of validate_ingredients to avoid circular imports between modules
    """
    from .validator import validate_ingredients
    validation = validate_ingredients(ingredients)

    if validation == f"{ingredients} - VALID":
        return f"Spell recorded: {spell_name} ({validation})"
    return f"Spell rejected: {spell_name} ({validation})"

