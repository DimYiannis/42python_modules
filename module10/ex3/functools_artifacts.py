from functools import reduce
import operator

def spell_reducer(spells: list[int], operation: str) -> int:
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
    pass
def memoized_fibonacci(n: int) -> int:
    pass
def spell_dispatcher() -> callable:
    pass


if __name__ == "__main__":

    spells =  [4 , 6, 8, 9, 856, 10, 3, 1, 2]
    print("\nTesting spell reducer...")
    print("Sum:",spell_reducer(spells, "add"))
    print("Multiplication:"spell_reducer(spells, "multiply"))
    print("Max:"spell_reducer(spells, "max"))
    print("Min:"spell_reducer(spells, "min"))
    print("Wrong input:"spell_reducer(spells, "div"))
