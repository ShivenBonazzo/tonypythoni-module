class Plant:
    """Classe base per tutte le piante."""
    plant_type = "regular"
    def __init__(self, name: str, height: int) -> None:
        """
        Costruttore della pianta base.
        Ogni pianta ha il proprio name e height.
        """
        self.name = name
        self.height = height
    
    def grow(self, cm: int) -> None:
        """
        Metodo di istanza: opera su QUESTA pianta specifica.
        """
        self.height += cm
        print(f"{self.name} grew {cm}cm")
    
    def get_info(self) -> str:
        """Restituisco info sulla pianta."""
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """
    Pianta che fiorisce. Eredita da Plant.
    Significa che ottiene gratis name, height, grow(), get_info().
    Aggiunge color e il concetto di fioritura (blooming).
    """
    plant_type = "flowering"
    def __init__(self, name: str, height: int, color: str) -> None:
        """
        super() si riferisce a Plant(il genitore diretto).
        Chiamando super().__init__(name, height) dici:
        "Fai tutto quello che fa il costruttore di Plant"
        Poi aggiungi gli attributi extra (color, is_blooming).
        Senza super(), name e height non verrebbero inizializzati.
        """
        super().__init__(name, height)
        self.color = color
        self.is_blooming = False
    
    def bloom(self) -> None:
        """Fa fiorire la pianta."""
        self.is_blooming = True
    
    def get_info(self) -> str:
        """
        Questo sovrascrive (override) il get_info() di Plant.
        Quando chiami flowering_plant.get_info(), Python usa QUESTO
        metodo, non quello di Plant, perche' e' piu' specifico.
        """
        bloom_status = "blooming" if self.is_blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers ({bloom_status})"


class PrizeFlower(FloweringPlant):
    """
    Fiore da competizione. Eredita da FloweringPlant.
    PrizeFlower ha TUTTO: name, height (da Plant), color, is_blooming,
    bloom() (da FloweringPlant), e in piu' prize_points (suo).
    """
    plant_type = "prize"
    def __init__(self, name: str, height: int,
                 color: str, prize_points: int) -> None:
        """
        super().__init__() qui chiama FloweringPlant.__init__(),
        che a sua volta chiama Plant.__init__().
        La catena di super() risale automaticamente.
        """
        super().__init__(name, height, color)
        self.prize_points = prize_points
    
    def get_info(self) -> str:
        """Sovrascrive get_info aggiunge i punti premio."""
        base_info = super().get_info()
        return f"{base_info}, Prize points: {self.prize_points}"


class GardenManager:
    """Gestore di un giardino con statistiche integrate."""

    total_gardens = 0

    def __init__(self, owner: str) -> None:
        """
        Costruttore del manager.

        TEORIA: self.plants e self.owner sono attributi di ISTANZA
        (ogni giardiano ha i propri). GardenManager.total_gardens e'
        un attributo di CLASSE (condiviso da tutti i giardini).
        """
        self.owner = owner
        self.plants: list = []
        self.total_growth: int = 0
        self.stats = self.GardenStats()
        GardenManager.total_gardens += 1

    class GardenStats:
        """Helper interno per calcolare statistiche del giardino."""

        def plant_count(self, plants: list) -> dict:
            """
            Conta le piante per tipo.
            isinstance(plant, PrizeFlower) controlla se un oggetto
            e' un'istanza di quella classe.
            L'ordine dei controlli conta: PrizeFlower PRIMA di 
            FloweringPlant, perche' un PrizeFlower e' anche un 
            FloweringPlant (ereditarieta'). Se controllassi 
            FloweringPlant prima, i PrizeFlower finirebbero nel
            conteggio sbagliato.
            """
            regular = 0
            flowering = 0
            prize = 0
            for plant in plants:
                if plant.plant_type == "prize":
                    prize += 1
                elif plant.plant_type == "flowering":
                    flowering += 1
                else:
                    regular += 1
            return {
                "regular": regular,
                "flowering": flowering,
                "prize": prize
            }
        
        def total_height(self, plants: list) -> int:
            """Calcola l'altezza totale di tutte le piante."""
            total = 0
            for plant in plants:
                total += plant.height
            return total
    
    def add_plant(self, plant: Plant) -> None:
        """Aggiunge una pianta a QUESTO giardino."""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")
    
    def grow_all(self, cm: int) -> None:
        """
        Fa crescere tutte le piante di questo giardino.
        self.plants e' la lista di QUESTO giardino.
        Se ho garden_alice e garden_bob, garden_alice.grow_all(1)
        fa crescere solo le piante di alice.
        """
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(cm)
            self.total_growth += cm
        
    def report(self) -> None:
        """Stampa il report di QUESTO giardino usando le stats interne."""
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"  - {plant.get_info()}")
        counts = self.stats.plant_count(self.plants)
        print(f"\nPlants added: {len(self.plants)}, "
              f"Total growth: {self.total_growth}cm")
        print(f"Plant types: {counts['regular']} regular, "
              f"{counts['flowering']} flowering, "
              f"{counts['prize']} prize flowers")
    
    def score(self) -> int:
        """Calcola il punteggio del giardino (somma altezze)."""
        return self.stats.total_height(self.plants)

    @classmethod
    def create_garden_network(cls, owners: list) -> list:
        """
        Crea una rete di giardini da una lista di nomi.
        """
        gardens = []
        for owner in owners:
            gardens.append(cls(owner))
        return gardens

    @staticmethod
    def is_valid_height(height: int) -> bool:
        """Controlla se un'altezza e' valida (non negativa)."""
        return height >= 0
    

if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    alice_garden = GardenManager("Alice")
    oak = Plant("Oak Tree", 140)
    rose = FloweringPlant("Rose", 25, "red")
    rose.bloom()
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    sunflower.bloom()
    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)
    alice_garden.grow_all(1)
    alice_garden.report()
    print(f"\nHeight validation test: {GardenManager.is_valid_height(50)}")
    bob_garden = GardenManager("Bob")
    bob_garden.add_plant(Plant("Fern", 50))
    bob_garden.add_plant(FloweringPlant("Tulip", 40, "pink"))
    bob_garden.grow_all(1)
    print(f"Garden scores - "
          f"{alice_garden.owner}: {alice_garden.score()}, "
          f"{bob_garden.owner}: {bob_garden.score()}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")
    

    