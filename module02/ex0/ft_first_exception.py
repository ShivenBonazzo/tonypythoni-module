def check_temperature(temp_str) -> None:
    try:
        value = int(temp_str)
        if value > 40:
            print(f"Error: {value}°C is too hot for plants (max 40°C)\n")
        elif value < 0:
            print(f"Error: {value}°C is too coold for plants (min 0°C)\n")
        else:
            print(f"Temperature {value}°C is perfect for plants!\n")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")


def test_temperature_input() -> None:
    print("Testing temperature: 25")
    check_temperature("25")
    print("Testing temperature: abc")
    check_temperature("abc")
    print("Testing temperature: 100")
    check_temperature("100")
    print("Testing temperature: -50")
    check_temperature("-50")


if __name__ == "__main__":
    print("=== Garden Temperature Check ===\n")
    test_temperature_input()

    print("All tests completed - program didn't crash!")
