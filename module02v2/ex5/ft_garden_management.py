class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants: list = []

    def add_plant(self, plant: str) -> None:
        if plant == "" or plant is None:
            raise PlantError("Plant name cannot be empty!")
        self.plants = self.plants + [plant]
        print(f"Added {plant} successfully my brotha!")

    def water_plants(self) -> None:
        try:
            print("\nWatering plants...")
            print("Opening watering system")
            for plant in self.plants:
                if plant is None:
                    raise WaterError("Cannot water None - invalid plant!")
                print(f"Watering {plant} - success")
        except WaterError as e:
            print(f"Error as {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant: str, water: int, sun: int) -> None:
        print("\nChecking plant health...")
        errors = ""
        if water < 1 or water > 10:
            errors = errors + "Water level needs to be between 1 and 10. "
        if sun < 2 or sun > 12:
            errors = errors + "Sunlight hours needs to be between 2 and 12. "
        if errors != "":
            raise ValueError(errors)
        print(f"{plant}: healthy (water: {water}, sun: {sun})")


def test_garden_management() -> None:
    print("===Garden Management System===")
    garden = GardenManager()
    print("\nAdding plants to garden...")
    for name in ["tomato", None, "lettuce", ""]:
        try:
            garden.add_plant(name)
        except PlantError as e:
            print(f"Error adding plant: {e}")
    garden.plants = garden.plants + [None]
    garden.water_plants()
    health_checks = [("tomato", 5, 8), ("lettuce", 15, 15)]
    for plant, water, sun in health_checks:
        try:
            garden.check_plant_health(plant, water, sun)
        except ValueError as e:
            print(f"Error checkin {plant}: {e}")
    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
