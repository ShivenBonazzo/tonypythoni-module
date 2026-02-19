import sys


def parse_inventory(args: list) -> dict:
    inventory: dict = {}
    i: int = 1
    while i < len(args):
        try:
            parts = args[i].split(":")
            key: str = parts[0]
            value: int = int(parts[1])
            inventory.update({key: value})
        except (ValueError, IndexError):
            print(f"Warning: '{args[i]}' is not valid, skipped.")
        i += 1
    return inventory


def get_total(inventory: dict) -> int:
    total: int = 0
    for value in inventory.values():
        total += value
    return total


def get_most_abundant(inventory: dict) -> str:
    most_key: str = ""
    most_val: int = -1
    for key, value in inventory.items():
        if value > most_val:
            most_val = value
            most_key = key
    return most_key


def get_least_abundant(inventory: dict) -> str:
    least_key: str = ""
    least_val: int = -1
    for key, value in inventory.items():
        if least_val == -1 or value < least_val:
            least_val = value
            least_key = key
    return least_key


def display_inventory(inventory: dict) -> None:
    total: int = get_total(inventory)
    items: list = []
    for key, value in inventory.items():
        items.append((key, value))
    i: int = 0
    while i < len(items) - 1:
        j: int = 0
        while j < len(items) - 1 - i:
            if items[j][1] > items[j + 1][1]:
                temp = items[j]
                items[j] = items[j + 1]
                items[j + 1] = temp
            j += 1
        i += 1
    for key, value in items:
        unit: str = "unit" if value == 1 else "units"
        percentage: float = round(value / total * 100, 1)
        print(f"{key}: {value} {unit} ({percentage}%)")


def display_categories(inventory: dict) -> None:
    moderate: dict = {}
    scarce: dict = {}
    for key, value in inventory.items():
        if value >= 5:
            moderate.update({key: value})
        else:
            scarce.update({key: value})
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")


def display_restock(inventory: dict) -> None:
    restock: list = []
    for key, value in inventory.items():
        if value <= 1:
            restock.append(key)
    if len(restock) > 0:
        print(f"Restock needed: {', '.join(restock)}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 ft_inventory_system.py item: quantity ...")
        return
    inventory: dict = parse_inventory(sys.argv)
    if len(inventory) == 0:
        print("No valid items provided.")
        return
    total: int = get_total(inventory)
    most: str = get_most_abundant(inventory)
    least: str = get_least_abundant(inventory)
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inventory)}")
    print("\n=== Current Inventory ===")
    display_inventory(inventory)
    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {most} ({inventory.get(most)} units)")
    print(f"Least abundant: {least} ({inventory.get(least)} unit)")
    print("\n=== Item Categories ===")
    display_categories(inventory)
    print("\n=== Management Suggestions ===")
    display_restock(inventory)
    print("\n=== Dictionary Properties Demo ===")
    keys_list: list = []
    for k in inventory.keys():
        keys_list.append(k)
    print(f"Dictionary keys: {', '.join(keys_list)}")
    values_list: list = []
    for v in inventory.values():
        values_list.append(str(v))
    print(f"Dictionary values: {', '.join(values_list)}")
    sample_key: str = keys_list[0]
    print(f"Sample lookup - '{sample_key}' in inventory: "
          f"{inventory.get(sample_key) is not None}")


if __name__ == "__main__":
    main()
