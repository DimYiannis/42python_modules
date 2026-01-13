


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda x: (spell1(x), spell2(x))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return lambda x: base_spell(x) * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    pass


def spell_sequence(spells: list[callable]) -> callable:
    pass


def add_two(x: int) -> int:
    result = x + 2
    return result

def add_3(x: int) -> int:
    result = x + 3
    return result


if __name__ == "__main__":
 
    result1 = spell_combiner(add_two, add_3)
    print(f"spell combiner:", result1(0))

    result2 = power_amplifier(add_3, 3)
    print("power_amplifier:", result2(0))



