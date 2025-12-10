def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        unit_type = "avalaible"
    elif unit == "grams":
        unit_type = "total"
    elif unit == "area":
        unit_type = "meters"
    else:
        unit_type = "Unknown unit type"
    print(f"{seed_type.capitalize()}: {quantity} {unit} {unit_type}")


# ft_seed_inventory("tomato", 15, "packets")
# ft_seed_inventory("carrot", 8, "grams")
# ft_seed_inventory("lettuce", 12, "area")
# ft_seed_inventory("bannanas", 100, "pieces")
