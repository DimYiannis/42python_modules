


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    lambda x: (spell1(x), spell2(x))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    pass


def conditional_caster(condition: callable, spell: callable) -> callable:
    pass


def spell_sequence(spells: list[callable]) -> callable:
    pass




if __name__ == "__main__":

