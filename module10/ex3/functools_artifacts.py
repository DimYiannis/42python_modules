from functools import reduce, partial
import operator

def spell_reducer(spells: list[int], operation: str) -> int:
    """
        reduce colapses the list of ints into one int
        takes the first 2 ints does the operation and
        what comes from them is used as first arg and
        keeps doing the operation with the first arg
        and the next one
    """
    if operation == "add":
        return reduce(operator.add, spells)
    elif operation == "multiply":
        return reduce(operator.mul, spells)
    elif operation == "max":
        return max(spells)
    elif operation == "min":
        return min(spells)
    else:
        print("unsupported operation")
        return None


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    """
        partial creates a new function by pre-filling 
        some arguments of an existing one, without calling it yet.
    """
    return  {
        #prefill by keyword
        'fire_enchant':  partial(base_enchantment, power = 50, element = "fire"),
        'ice_enchant': partial(base_enchantment, power = 50, element = "ice"),
        #prefill by position
        'lightning_enchant': partial(base_enchantment, 50, "lightning")

    }
    

def memoized_fibonacci(n: int) -> int:
    pass
def spell_dispatcher() -> callable:
    pass





def base_enchantment(power, element, target):
    """
        return nested dict
    """
    result = {target: {"power": power, "element": element}}
    print(f" weapon {target} with power {power} and elemnt type {element}")
    return result

if __name__ == "__main__":

    spells =  [4 , 6, 8, 9, 856, 10, 3, 1, 2]
    print("\nTesting spell reducer...")
    print("Sum:",spell_reducer(spells, "add"))
    print("Multiplication:",spell_reducer(spells, "multiply"))
    print("Max:",spell_reducer(spells, "max"))
    print("Min:",spell_reducer(spells, "min"))
    print("Wrong input:",spell_reducer(spells, "div"))

    print("\nTesting partial_enchanter...")
    bro = partial_enchanter(base_enchantment)
    bro["fire_enchant"](target = "phoenix")
    bro["ice_enchant"](target ="polarbear")
    bro["lightning_enchant"]("thorrr")
