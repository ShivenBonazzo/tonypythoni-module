class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant(name: str) -> None:
    if name == "tomato":
        raise PlantError("The tomato plant is wilting!")
    print(f"{name} is doing fine")


def check_water(level: int) -> None:
    if level < 3:
        raise WaterError("Not enough water in the tank!")
    print(f"Water level {level} is ok")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        check_plant("tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        check_water(1)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("\nTesting catching all garden errors...")
    try:
        check_plant("tomato")
    except GardenError as e:
        print(f"Caught a garden Error: {e}")
    try:
        check_water(1)
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
