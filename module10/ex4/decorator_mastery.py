import time
from functools import wraps

def spell_timer(func: callable) -> callable:

    @wraps(func)
    def wrapper(*args, **kwargs):

        print(f"Casting {func.__name__}...")

        begin = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"Spell completed in {end - begin:.6f} seconds")
        return result
 
    return wrapper

def power_validator(min_power: int) -> callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if "power" in kwargs:
                power = kwargs["power"]
            else:
                power = args[-1]

            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            counter = 1
            while counter <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if counter < max_attempts:
                        print(f"spell failed, retrying... (attempt {counter}/{max_attempts})")
                    counter += 1
            return f"spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False

        for char in name:
            if not (char.isalpha() or char.isspace()):
                return False

        return True
    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"succesfully cast {spell_name} with power {power}"

# to be decorated
def fireball():
    print("Fireball cast!")

@power_validator(50)
def cast_spell(power):
    return f"spell cast with power {power}"

@retry_spell(3)
def unstable_spell():
    raise ValueError("spell fizzled!")



if __name__ == "__main__":

    print("\nTesting spell timer...")
    fireball = spell_timer(fireball)

    val = fireball()
    print(val)

    print("\nTesting power validator")
    print(cast_spell(30))
    print(cast_spell(70))

    print("\nTesting retry_spell")
    result = unstable_spell()
    print(result)

    print("\nTesting MageGuild... ")
    check = MageGuild()
    print(check.cast_spell("aaa", 15))
    print(check.cast_spell("aa", 5))
    check_power = MageGuild.cast_spell
    print(check.cast_spell(spell_name="aha", power=100))
    print(check.cast_spell(spell_name="ahem", power=10))
