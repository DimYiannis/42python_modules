"""
using exception like before for custom errors

"""


class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass

    """
    class where we initialise a dict
     we have 3 methods where we add
     a plant, water the plants and check
     if the plants have been watered
    """


class GardenManager:
    def __init__(self):
        self.plants = {}

    def add_plant(self, plant_name, water_lvl=5, sunlt_hrs=8):
        try:
            if plant_name is None or plant_name == "":
                raise PlantError("Plant name cannot be empty!")
            self.plants[plant_name] = {"water": water_lvl, "sun": sunlt_hrs}
            print(f"Added {plant_name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self):
        print("Opening watering system")
        try:
            for plant in self.plants:
                if self.plants[plant]["water"] <= 0:
                    raise WaterError("Not enough water in tank")
                print(f"Watering {plant} - success")
        except WaterError as e:
            print(f"Caught GardenError: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name):
        """
        throw err if name is not okk
        throw err if water level is not okk
        throw err if both are not okk
        """
        try:
            if plant_name not in self.plants:
                raise PlantError(f"{plant_name} not found in garden!")
            plant = self.plants[plant_name]
            water = plant["water"]
            sun = plant["sun"]

            if water < 1:
                raise ValueError(f"Water amount {water} is too low (min 1)")
            elif water > 10:
                raise ValueError(f"Water amount {water} is too high (max 10)")

            if sun < 2:
                raise ValueError(f"Sunlight hours {sun} is too low (min 2)")
            elif sun > 12:
                raise ValueError(f"Sunlight hours {sun} is too high (max 12)")

            print(f"{plant_name}: healthy (water: {water}, sun: {sun})")
        except (PlantError, ValueError) as e:
            print(f"Error checking {plant_name}: {e}")


def test_garden_manager():
    print("=== Garden Management System ===\n")
    manager = GardenManager()

    print("Adding plants to garden...")
    manager.add_plant("tomato")
    manager.add_plant("lettuce", water_lvl=15)
    manager.add_plant("")

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    for plant_name in manager.plants:
        manager.check_plant_health(plant_name)

    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


test_garden_manager()
