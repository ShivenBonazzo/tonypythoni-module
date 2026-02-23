def check_plant_health(
        plant_name: str, water_level: int, sunlight_hours: int
        ) -> str:
    if plant_name is None:
        raise ValueError("Plant name cannot be empty!")
    if water_level < 1 or water_level > 10:
        raise ValueError("water level needs to be between 1 and 10")
    if sunlight_hours < 2 or sunlight_hours > 12:
        raise ValueError("Sunlight hours needs to be between 2 and 12")
    return f"plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values")
    try:
        print(check_plant_health("cicciopasticcio", 2, 3))
    except ValueError:
        print("Questo non lo stampero' mai")
    print("\nTesting empty plant name...")
    try:
        print(check_plant_health(None, 2, 3))
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTesting bad water level...")
    try:
        print(check_plant_health("casd", -12, 3))
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTesting bad sunlight hours...")
    try:
        print(check_plant_health("ciao", 2, -3))
    except ValueError as e:
        print(f"Error: {e}")
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
