


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """
        sort based on power
        needed to use reverse so that the order is reversed
        sorted function creates a new list!
    """
    result = sorted(artifacts, key=lambda x: x["power"], reverse=True)
    return result


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """
        filter based on the value of power
        filter doesnt retun a list!
        so we also need to use list
    """
    result = list(filter(lambda x: x["power"] >= min_power, mages))
    return result


def spell_transformer(spells: list[str]) -> list[str]:
    """
    adding * as prefix and sufix
    """
    result = list(map(lambda x: '*' + x + '*', spells))
    return result


def mage_stats(mages: list[dict]) -> dict:
    """
        cant use lambda in sum 
        used round func to determine the number of decimals
    """
    strongest = max(mages, key=lambda x: x['power'])
    weakest = min(mages, key=lambda x: x['power'])
    avg_power = round(sum(x['power'] for x in mages) / len(mages), 2)
    result = {'max_power': strongest, 'min_power': weakest, 'avg_power': avg_power}
    return result


if __name__ == "__main__":
    artifacts = [
        {"name": "Orb of Fire", "power": 90, "type": "fire"},
        {"name": "Frost Wand", "power": 70, "type": "ice"},
        {"name": "Shadow Cloak", "power": 85, "type": "dark"},
    ]

    names = [
        "Ariana", "Kai", "Luna", "Ezra", "Maya",
        "Finn", "Nova", "Leo", "Isla", "Jasper",
        "Elara", "Ronan", "Soren", "Freya", "Atlas",
        "Clara", "Orion", "Ivy", "Dashiell", "Zara"
    ]
    print("\nTesting artifact sorter...")
    print("\nartifact sorter:", artifact_sorter(artifacts))
    print("\npower filter:", power_filter(artifacts, 85))
    print("\nspell transformer:", spell_transformer(names))

    print("\nmage stats:")
    stats = mage_stats(artifacts)
    print(f"max power:{stats['max_power']}")
    print(f"min power:{stats['min_power']}")
    print(f"avg power:{stats['avg_power']}")
