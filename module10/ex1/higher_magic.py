


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda x: (spell1(x), spell2(x))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return lambda x: base_spell(x) * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    return lambda x: spell(x) if condition(x) == True else "Spell fizzled"


def spell_sequence(spells: list[callable]) -> callable:
    return lambda x: [f(x) for f in spells]
# could also do list(map(lambda f: f(x), spells ))


def add_two(x: int) -> int:
    result = x + 2
    return result

def add_3(x: int) -> int:
    result = x + 3
    return result

def maybe(num): 
    if num % 2 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
 
    result1 = spell_combiner(add_two, add_3)
    print("\nTesting spell combiner:")
    print("spell combiner result:", result1(0))

    result2 = power_amplifier(add_3, 3)
    print("\nTetsing power amplifier:")
    print("power_amplifier result:", result2(0))

    #checking if maybe works correctly and then proceed with the function
    print(maybe(3))
    result3 = conditional_caster(maybe, add_two)
    print("\nTesting conditional_caster:")
    print("conditional_caster result", result3(3))

    listt = [add_two, add_3, maybe]
    result4 = spell_sequence(listt)
    print("\nTesting spell_sequence")
    print("spell sequence result:",result4(2))







