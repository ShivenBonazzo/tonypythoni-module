def water_plants(plant_list: list) -> None:
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                raise ValueError("Error: Cannot water None - invalid plant!")
            else:
                print(f"Watering {plant}")
    except ValueError as e:
        print(f"{e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    plant_list = ["tomato", "lettuce", "carrots"]
    print("\nTesting normal watering...")
    water_plants(plant_list)
    print("Watering completed successfully!")
    print("\nTesting with error...")
    list_error = ["tomato", None, "carrots"]
    water_plants(list_error)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    test_watering_system()
