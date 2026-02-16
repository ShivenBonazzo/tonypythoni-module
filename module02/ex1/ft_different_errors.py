def garden_operations() -> None:
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print("\nTesting ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print("\nTesting FileNotFoundError...")
    try:
        file = open("missing.txt")
        file.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    print("\nTesting KeyError...")
    try:
        plants = {"ciccio": 1}
        plants["missing_plant"]
    except KeyError:
        print("Caught KeyError: 'missing_plant'")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("\nTesting multiple errors together...")
    try:
        int("abc")
    except (ValueError, ZeroDivisionError, FileNotFoundError):
        print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
