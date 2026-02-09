class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    pianta1 = Plant("Rose", 25, 30)
    pianta2 = Plant("Oak", 200, 365)
    pianta3 = Plant("Cactus", 5, 90)
    pianta4 = Plant("Sunflower", 80, 45)
    pianta5 = Plant("Fern", 15, 120)
    print("\nTotal plants created: 5")
