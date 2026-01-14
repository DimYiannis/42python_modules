from functools import reduce, partial, lru_cache, singledispatch
import operator
import time

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

@lru_cache(maxsize = 128)
def memoized_fibonacci(n: int) -> int:
    """
        using lru_cache decorator
        to help reduce the execution time
    """
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)



def spell_dispatcher() -> callable:

    @singledispatch
    def spell(arg):
        print("default:")

    @spell.register(int)
    def damage_spell(arg: int):
        print(f"spell's damage is {arg}")

    @spell.register(str)
    def enchantment(arg: str):
        print(f"spell's enchantment is {arg}")

    @spell.register(list)
    def multi_cast(arg: list):
        print(f"items in list:", end=" ")
        for item in arg:
            print(item, end=", ")

    return spell




def base_enchantment(power, element, target):
    """
        return nested dict
    """
    result = {target: {"power": power, "element": element}}
    print(f" weapon {target} with power {power} and elemnt type {element}")
    return result


def fib_without_cache(n):
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


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

    print("\nTesting memoized fibonacci...")

    n1 = 10

    begin = time.time()
    print(f"Fib({n1})", memoized_fibonacci(n1))
    end = time.time()
    print("Time taken to execute the function with lru_cache is", end-begin)

    begin = time.time()
    print(f"Fib({n1})", fib_without_cache(n1))
    end =time.time()
    print("Time taken to execute the function without lru_cache is", end-begin)

    n2 = 15

    begin = time.time()
    print(f"Fib({n2})", memoized_fibonacci(n2))
    end = time.time()
    print("Time taken to execute the function with lru_cache is", end-begin)

    begin = time.time()
    print(f"Fib({n2})", fib_without_cache(n2))
    end = time.time()
    print("Time taken to execute the function without lru_cache is", end-begin)


    print("\nTesting multi_cast...")
    cars = ['audi', 'bmw', 'honda']
    callme = spell_dispatcher()
    callme(2)
    callme("bruh")
    callme(cars)
