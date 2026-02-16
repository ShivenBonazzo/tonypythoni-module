class Plant:
    """Class of a Plant"""
    def __init__(self, name, height, age) -> None:
        """Info of a Plant"""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Class of a Flower"""
    def __init__(self, name, height, age, color) -> None:
        """Info of a Flower"""
        super().__init__(name, height, age)
        self.color = color
        print(
            f"{self.name} (Flower): {self.height}cm, "
            f"{self.age} days, {self.color} color")

    def bloom(self) -> None:
        """Flower blooming"""
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    """Class of a Tree"""
    def __init__(self, name, height, age, diameter) -> None:
        """Info of a Tree"""
        super().__init__(name, height, age)
        self.diameter = diameter
        print(
            f"{self.name} (Tree): {self.height}cm, "
            f"{self.age} days, {self.diameter}cm diameter")

    def produce_shade(self) -> None:
        """Produce shade"""
        shade_area = int(3.14159 * (self.diameter / 2))
        print(f"{self.name} provides {shade_area} square meters of shade\n")


class Vegetable(Plant):
    """Class of a vegetable"""
    def __init__(
            self, name, height, age, harvest_season, nutritional_value
            ) -> None:
        """Info of a vegetable"""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print(
            f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
            f"{self.harvest_season} harvest \n{self.name} "
            f"is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    fiore = Flower("Rose", 25, 30, "red")
    fiore.bloom()
    albero = Tree("Oak", 500, 1825, 50)
    albero.produce_shade()
    verdura = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
