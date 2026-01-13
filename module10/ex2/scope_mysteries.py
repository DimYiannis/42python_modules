


def mage_counter() -> callable:
    count = 0
    """
        -tried to use nonlocal in a lambda func
        but its not possible it gives syntax error
        -so i used closure to maintain state 
        without global var
    """
    def counter():
        """
            used nonlocal for enclosing Scope 
            Variables in an enclosing function but not global
        """
        nonlocal count 
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> callable:
    
    base_power = initial_power
    
    def increase():
        nonlocal base_power
        base_power += 150
        return base_power
    return increase


def enchantment_factory(enchantment_type: str) -> callable:
    def inner(item: str):
        print(f"{enchantment_type} {item}")
    return inner


def memory_vault() -> dict[str, callable]:

    data = {}

    def store(key: str, value):
        nonlocal data
        data["key"] = value

    def recall(key: str):
        nonlocal data
        for item in data:
            if data.get('key') == key


if __name__ == "__main__":

    print("\nTesting mage counter:")
    c = mage_counter()
    for num in range(1,4):
        print(f"Call {num}:", c())

    print("\nTetsing spell_accumulator:")
    inner = spell_accumulator(0)
    for i in range(1,4):
        print(f"Call {i}:", inner())

    print("\nTesting enchantment_factory:")
    Flaming = enchantment_factory("Flaming")
    Frozen = enchantment_factory("Frozen")
    Flaming("sword")
    Frozen('shield')
    Flaming('potion')

    print("\nTesting memory_vault")


