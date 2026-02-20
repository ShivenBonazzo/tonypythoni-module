def garden_operations() -> None:
    try:
        print("\nTesting ValueError...")
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    try:
        print("\nTesting ZeroDivisionError...")
        10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    try:
        print("\nTesting FileNotFoundError...")
        file = open("cicciobello.txt")
        file.close()
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    try:
        print("\nTesting KeyError...")
        dictionary = {"ciccio": 1}
        dictionary["manca key"]
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    try:
        print("\nTesting multiple errors together...")
        int("cicciobellohalabuaevuolete")
    except (ValueError, ZeroDivisionError, KeyError):
        print("Caught an error, but program continues!")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
