class Plant:
    """Info of a Plant"""
    name: str
    height: int
    age: int


if __name__ == "__main__":
    pianta1 = Plant()
    pianta2 = Plant()
    pianta3 = Plant()
    pianta1.name = "Rose"
    pianta1.height = 25
    pianta1.age = 30
    pianta2.name = "Sunflower"
    pianta2.height = 80
    pianta2.age = 45
    pianta3.name = "Cactus"
    pianta3.height = 15
    pianta3.age = 120
    print("=== Garden Plant Registry ===")
    print(f"{pianta1.name}: {pianta1.height}cm, {pianta1.age} days old")
    print(f"{pianta2.name}: {pianta2.height}cm, {pianta2.age} days old")
    print(f"{pianta3.name}: {pianta3.height}cm, {pianta3.age} days old")
