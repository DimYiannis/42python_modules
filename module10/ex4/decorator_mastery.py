import time
from functools import wraps

def spell_timer(func: callable) -> callable:


    #before execution
    print("Casting function_name...")

    @wraps(func)
    def wrapper(*args, **kwargs):
        begin = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        #after execution
        print("Spell completed in time seconds")
        return result
 
    return wrapper

def power_validator(min_power: int) -> callable:
    pass


def retry_spell(max_attempts: int) -> callable:
    pass


class MageGuild:


@staticmethod
def validate_mage_name(name: str) -> bool:
    pass

def cast_spell(self, spell_name: str, power: int) -> str:
    pass
