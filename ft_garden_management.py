class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants = {}

    def add_plant(self, plant_name, water_level=5, sunlight_hours=8):
        try:
            if not plant_name or plant_name.strip() == "":
                raise PlantError("Plant name cannot be empty!")
            self.plants[plant_name] ={"water": water_level, "sun": sunlight_hours}
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
        try:
            if plant_name not in self.plants:
                raise PlantError(f"{plant_name} not found in garden!")
            plant = self.plants[plant_name]
            water = plant["water"]
            sun = plant["sun"]

            if not (1 <= water <= 10):
                raise ValueError(
                    f"Water level {water} is too"
                    f"{'low' if water < 1 else 'high'}"
                    f"(min 1, max 10)"
                )
            if not (2 <= sun <= 12):
                raise ValueError(
                    f"Sunlight hours {sun} is too"
                    f"{'low' if sun < 2 else 'high'} (min 2, max 12)"
                )

            print(f"{plant_name}: healthy (water: {water}, sun: {sun})")
        except (PlantError, ValueError) as e:
            print(f"Error checking {plant_name}: {e}")


def test_garden_manager():
    print("=== Garden Management System ===")
    manager = GardenManager()

    print("Adding plants to garden...")
    manager.add_plant("tomato")
    manager.add_plant("lettuce", water_level=15)
    manager.add_plant("")

    print("Watering plants...")
    manager.water_plants()

    print("Checking plant health...")
    for plant_name in manager.plants:
        manager.check_plant_health(plant_name)

    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("Garden management system test complete!")


test_garden_manager()
