


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
    pass


def mage_stats(mages: list[dict]) -> dict:
    pass


if __name__ == "__main__":
    artifacts = [
        {"name": "Orb of Fire", "power": 90, "type": "fire"},
        {"name": "Frost Wand", "power": 70, "type": "ice"},
        {"name": "Shadow Cloak", "power": 85, "type": "dark"},
    ]

    print("\nTesting artifact sorter...")
    print("\nartifact sorter:", artifact_sorter(artifacts))
    print("\npower filter:", power_filter(artifacts, 85))
