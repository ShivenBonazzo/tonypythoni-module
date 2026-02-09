class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.__name = name
        self.__height = height
        self.__age = age
        print(f"Plant created: {self.__name}")

    def set_height(self, height) -> None:
        if height >= 0:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(
                "\nInvalid operation attempted:"
                f"height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age) -> None:
        if age >= 0:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")
        else:
            print(
                "\nInvalid operation attempted:"
                f"age {age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_name(self) -> int:
        return self.__name

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    pianta = SecurePlant("Rose", 20, 30)
    pianta.set_height(25)
    pianta.set_age(30)
    pianta.set_height(-5)
    print(
        f"\nCurrent plant: {pianta.get_name()}"
        f"({pianta.get_height()}cm, {pianta.get_age()} days)")
