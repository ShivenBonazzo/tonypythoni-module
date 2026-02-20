class GardenManager:
    def __init__(self) -> None:
        self.plants: list = []

    def add_plants(self, plant: str) -> None:
        self.plants = self.plants + [plant]
        print(f"Added {plant} successfully!")

    def water_plants(self) -> None:
        for plant in self.plants:
            print(f"Watering {plant} - success")
    
    def check_plant_health(self, plant)


