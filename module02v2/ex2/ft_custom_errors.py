class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant() -> None:
    print("\nTesting PlantError...")
    plant = input("Choose your plant: ")
    try:
        if plant == "tomato":
            raise PlantError("The tomato plant is wiltin!")
        elif plant is None or plant == "":
            raise PlantError(" invalid name")
        else:
            print(
                f"{plant} is a fantastic name"
                " for a plant and he is all good!"
                )
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def check_water() -> None:
    print("\nTesting WaterError...")
    water = input("How much water do you wanna put? ")
    try:
        if int(water) > 2:
            print("Yo is too much my brotha")
        elif 0 < int(water) <= 2:
            print("Good choice my brotha")
        elif int(water) <= 0:
            raise WaterError("My brotha is trolling me")
    except WaterError as e:
        print(f"{e}")
    except ValueError:
        print("Yo my brotha don't know what is a number")


def check_garden() -> None:
    print("\nTesting catching all garden errors...")
    plant = input("Choose your plant: ")
    try:
        if plant == "tomato":
            raise PlantError("Caught PlantError: The tomato plant is wiltin!")
        elif plant is None or plant == "":
            raise PlantError("invalid plant")
        else:
            print(
                f"{plant} is a fantastic name"
                " for a plant and he is all good!"
                )
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    water = input("How much water do you wanna put? ")
    try:
        if int(water) > 2:
            print("Yo is too much my brotha")
        elif 0 < int(water) <= 2:
            print("Good choice my brotha")
        elif int(water) <= 0:
            raise WaterError("My brotha is trolling me")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    except ValueError:
        print("Yo my brotha don't know what is a number")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    check_plant()
    check_water()
    check_garden()
    print("\nAll custom error types work correctly my brotha!")
