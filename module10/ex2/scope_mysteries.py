


def mage_counter() -> callable:
    count = 0
    """
        -tried to use nonlocal in a lambda func
        but its not possible it gives syntax error
        -so i used closure to maintain state 
        without global var
    """
    def counter():
        nonlocal count += 1
        return count
    return counter 


def spell_accumulator(initial_power: int) -> callable:
    pass


def enchantment_factory(enchantment_type: str) -> callable:
    pass


def memory_vault() -> dict[str, callable]:
    pass



if __name__ == "__main__":

    for num in range(0,5):
        print(mage_counter)
