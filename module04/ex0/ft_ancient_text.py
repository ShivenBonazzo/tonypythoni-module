import sys


def recover_ancient_text(filename: str) -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print(f"\nAccessing Storage Vault: {filename}")
    vault = open(filename, "r")
    print("Connection established...")
    print("\nRECOVERED DATA:")
    content = vault.read()
    lines = content.strip().split("\n")
    i = 1
    for line in lines:
        print(f"[FRAGMENT {i:03d}] {line}")
        i = i + 1
    print("\nData recovery complete. Storage unit disconnected.")


def main() -> None:
    filename = "acient_fragment.txt"
    try:
        recover_ancient_text(filename)
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        sys.exit(1)


if __name__ == "__main__":
    main()
