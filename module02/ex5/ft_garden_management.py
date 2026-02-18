class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants = {}

    def add_plant(self, name: str) -> None:
        if name == "":
            raise PlantError("Plant name cannot be empty!")
        self.plants[name] = {"water": 5, "sun": 8}
        print(f"Added {name} successfully")

    def water_plants(self) -> None:
        try:
            print("Opening watering system")
            for name in self.plants:
                print(f"Watering {name} - success")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self, name: str, water: int, sun: int) -> None:
        if water < 1 or water > 10:
            raise ValueError(f"Water level {water} is too high (max 10)")
        print(f"{name}: healthy (water: {water}, sun: {sun})")


def test_garden_management() -> None:

    print("=== Garden Management System ===")
    garden = GardenManager()
    print("\nAdding plants to garden...")
    for name in ["tomato", "lettuce", ""]:
        try:
            garden.add_plant(name)
        except PlantError as e:
            print(f"Error adding plant: {e}")
    print("\nWatering plants...")
    garden.water_plants()
    print("\nChecking plant health...")
    health_checks = [("tomato", 5, 8), ("lettuce", 15, 8)]
    for name, water, sun in health_checks:
        try:
            garden.check_health(name, water, sun)
        except ValueError as e:
            print(f"Error checkin {name}: {e}")
    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
