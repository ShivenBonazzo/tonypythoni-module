def garden_operations() -> None:
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    try:
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    try:
        file = open("missing.txt")
        file.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    try:



def test_error_types() -> None:
    garden_operations()


if __name__ == "__main__":
    test_error_types()
