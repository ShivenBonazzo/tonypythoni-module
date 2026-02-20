def check_temperature(temp_str) -> None:
    try:
        print(f"\nTesting temperature: {temp_str}")
        if 0 <= int(temp_str) <= 40:
            print(f"Temperature {temp_str}°C is perfect for plants!")
        elif int(temp_str) < 0:
            print(f"Error: {temp_str}°C is too cold for plants (min 0°C)")
        elif int(temp_str) > 40:
            print(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
    except ValueError:
        print(f"Error '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
