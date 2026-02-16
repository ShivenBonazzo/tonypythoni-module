class Plant:
    """Info of a Plant"""
    name: str
    height: int
    age_plant: int

    def grow(self) -> None:
        """Grow plant +1"""
        self.height += 1

    def age(self) -> None:
        """Age plant +1"""
        self.age_plant += 1

    def get_info(self) -> None:
        """Get info plant"""
        print(f"{self.name}: {self.height}cm, {self.age_plant} days old")


if __name__ == "__main__":
    print("=== Day 1 ===")
    pianta = Plant()
    pianta.name = "Rose"
    pianta.height = 25
    pianta.age_plant = 30
    pianta.get_info()
    for days in range(6):
        pianta.grow()
        pianta.age()
    print("=== Day 7 ===")
    pianta.get_info()
    print(f"Growth this week: {days + 1}cm")
