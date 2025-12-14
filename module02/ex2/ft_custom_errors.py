class GardenError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


class PlantError(GardenError):
    def __init__(self, message):
        GardenError.__init__(self, message)


class WaterError(GardenError):
    def __init__(self, message):
        GardenError.__init__(self, message)


def check_plant():
    raise PlantError("The tomato plant is wilting!")


def check_water():
    raise WaterError("Not enough water in the tank!")


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        check_plant()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("Testing WaterError...")
    try:
        check_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("Testing catching all garden errors...")
    try:
        check_plant()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        check_water()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("All custom error types work correctly!")


test_custom_errors()
